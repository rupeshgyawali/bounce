import time

class Game_Over:
	def __init__(self, tk, canvas, target):
		self.canvas = canvas
		self.tk = tk
		self.text1 = self.canvas.create_text(350, 200, text = 'Game Over!',\
		 font = ('Times', 50))
		self.text2 = self.canvas.create_text(350, 250, text = 'Your Score: ' + \
		 str(target.total), font = ('Snap ITC', 20))
		self.text3 = self.canvas.create_text(300, 300, text = 'Restart',\
		 font = ('Arial', 20))
		self.text4 = self.canvas.create_text(400, 300, text = 'Exit',\
		 font = ('Arial', 20))
		self.point = self.canvas.create_polygon(10, 10, 15, 15, 10, 20)
		self.canvas.move(self.point, 235, 285)
		self.restart = False
		self.exit = False
		with open('data', 'r+') as f:
			high_score = f.read(2)
			if target.total > int(high_score):
				self.canvas.move(self.text1,1000,1000)
				self.text1 = self.canvas.create_text(350, 200, text = \
					'High Score!',font = ('Times', 50))
				f.seek(0)
				f.write(str(target.total))
		self.canvas.bind_all('<KeyPress-Left>', self.pointer)
		self.canvas.bind_all('<KeyPress-Right>', self.pointer)
		self.canvas.bind_all('<KeyPress-Return>', self.pointer)

	def pointer(self,evt):
		self.point_pos = self.canvas.coords(self.point)
		if evt.keysym == 'Left':
			if self.point_pos[0] > 260:
				self.canvas.move(self.point, -125, 0)
			else:
				self.canvas.move(self.point, 125, 0)
		elif evt.keysym == 'Right':
			if self.point_pos[0] < 260:
				self.canvas.move(self.point, 125, 0)
			else:
				self.canvas.move(self.point, -125, 0)
		elif evt.keysym == 'Return':
			if self.point_pos[0] > 260:
				self.exit = True
			else:
				self.restart = True
	
	def over_loop(self):
		while 1:
			if self.restart == True:
				self.canvas.move(self.text1, 1000, 1000)
				self.canvas.move(self.text2, 1000, 1000)
				self.canvas.move(self.text3, 1000, 1000)
				self.canvas.move(self.text4, 1000, 1000)
				self.canvas.move(self.point, 1000, 1000)
				self.tk.update()
				break
			if self.exit == True:
				break
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.1)

class Game_Complete:
	def __init__(self, tk, canvas, target):
		self.canvas = canvas
		self.tk = tk
		self.text1 = self.canvas.create_text(350, 200, text = 'High Score!', \
			font = ('Times', 50))
		self.text2 = self.canvas.create_text(350, 250, text = 'Your Score: ' + \
			str(target.total), font = ('Snap ITC', 20))
		self.text3 = self.canvas.create_text(300, 300, text = 'Restart',\
		 font = ('Arial', 20))
		self.text4 = self.canvas.create_text(400, 300, text = 'Exit',\
		 font = ('Arial', 20))
		self.point = self.canvas.create_polygon(10, 10, 15, 15, 10, 20)
		self.canvas.move(self.point, 235, 285)
		self.restart = False
		self.exit = False
		with open('data', 'w') as f:
			f.seek(0)
			f.write(str(target.total))
		self.canvas.bind_all('<KeyPress-Left>', self.pointer)
		self.canvas.bind_all('<KeyPress-Right>', self.pointer)
		self.canvas.bind_all('<KeyPress-Return>', self.pointer)

	def pointer(self,evt):
		self.point_pos = self.canvas.coords(self.point)
		if evt.keysym == 'Left':
			if self.point_pos[0] > 260:
				self.canvas.move(self.point, -125, 0)
			else:
				self.canvas.move(self.point, 125, 0)
		elif evt.keysym == 'Right':
			if self.point_pos[0] < 260:
				self.canvas.move(self.point, 125, 0)
			else:
				self.canvas.move(self.point, -125, 0)
		elif evt.keysym == 'Return':
			if self.point_pos[0] > 260:
				self.exit = True
			else:
				self.restart = True
	
	def over_loop(self):
		while 1:
			if self.restart == True:
				self.canvas.move(self.text1, 1000, 1000)
				self.canvas.move(self.text2, 1000, 1000)
				self.canvas.move(self.text3, 1000, 1000)
				self.canvas.move(self.text4, 1000, 1000)
				self.canvas.move(self.point, 1000, 1000)
				self.tk.update()
				break
			if self.exit == True:
				break
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.1)

