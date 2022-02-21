from tkinter import *
import random
import time

class Game:
	def __init__(self):
		self.tk = Tk()
		self.tk.title('Play')
		self.tk.resizable(0, 0)
		self.tk.wm_attributes('-topmost', 1)
		self.canvas = Canvas(self.tk, width = 700, height = 500, bd = 0,\
			highlightthickness = 0)
		self.canvas.pack()
		self.tk.update()

	def main_loop(self, ball, paddle, target):
		while 1:
			if ball.hit_bottom == True or target.complete == True:
				break
			ball.move_ball()
			paddle.move_paddle()
			target.hit_target()
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.01)

class Ball(Game):
	def __init__(self, canvas, paddle):
		self.canvas = canvas
		self.paddle = paddle
		self.id = self.canvas.create_oval(10, 10, 30, 25, fill = 'Red')
		self.canvas.move(self.id, 200, 100)
		self.canvas.update()
		starts = [-3, -2, -1, 1, 2, 3]
		self.x = random.choice(starts)
		self.y = -1
		self.canvas_width = self.canvas.winfo_width()
		self.canvas_height = self.canvas.winfo_height()
		self.hit_bottom = False

	def move_ball(self):
		self.canvas.move(self.id, self.x, self.y)
		self.pos = self.canvas.coords(self.id)
		if self.pos[0] <= 0:
			self.x = 2
		if self.pos[2] >= self.canvas_width:
			self.x = -2
		if self.pos[1] <= 0:
			self.y = 1
		if self.pos[3] >= self.canvas_height:
			self.hit_bottom = True
		if self.hit_paddle(self.pos) == True:
			self.y = -3
			

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[0] <= paddle_pos[2] and pos[2] >= paddle_pos[0]:
			if pos[1] <= paddle_pos[3] and pos[3] >= paddle_pos[1]:
				return True
		return False

class Paddle(Game):
	def __init__(self, canvas):
		self.canvas = canvas
		self.id = self.canvas.create_rectangle(10, 10, 100, 20, fill = \
			"Blue")
		self.canvas.move(self.id, 350, 400)
		start = [-2, 2]
		self.x = random.choice(start)
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>', self.left)
		self.canvas.bind_all('<KeyPress-Right>', self.right)

	def move_paddle(self):
		self.canvas.move(self.id, self.x, 0)
		self.pos = self.canvas.coords(self.id)
		if self.pos[0] <=0:
			self.x = 2
		if self.pos[2] >= self.canvas_width:
			self.x = -2

	def left(self,evt):
		self.x = -2

	def right(self,evt):
		self.x = 2

class Target(Game):
	def __init__(self, canvas, ball):
		self.canvas = canvas
		self.ball = ball
		self.total = 0
		self.complete = False
		self.id_list = []
		x = 25
		y = 20
		for i in range(1, 66):
			self.id = self.canvas.create_rectangle(x, y, x + 40 \
				, y + 10, fill = 'Green')
			if i % 13 == 0:
				y += 15
				x = 25
			else:
				x += 50
			self.id_list.append(self.id)

	def hit_target(self):
		ball_pos = self.canvas.coords(self.ball.id)
		for i in self.id_list:
			target_pos = self.canvas.coords(i)
			if ball_pos[0] <= target_pos[2] and ball_pos[2] >= target_pos[0]:
				if ball_pos[1] <= target_pos[3] and ball_pos[3] >= target_pos[1]:
					self.canvas.move(i, 1000, 1000)
					self.total += 1
		if self.total == 65:
			self.complete =True
