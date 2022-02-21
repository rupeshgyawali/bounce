import time

class Game_Start:
	def __init__(self, tk, canvas):
		self.canvas = canvas
		self.tk = tk
		self.text1 = self.canvas.create_text(350, 150, text = 'Bounce!',\
		 font = ("Times", 50))
		self.text2 = self.canvas.create_text(350, 200, text = 'Play' + ' ' * 10,\
		 font = ("Arial", 20))
		self.text3 = self.canvas.create_text(350, 260, text = 'Help' + ' ' * 10,\
		 font = ("Arial", 20))
		self.text4 = self.canvas.create_text(350, 290, text = 'Exit' + ' ' * 11,\
		 font = ("Arial", 20))
		self.text5 = self.canvas.create_text(350, 320, text = 'About' + ' ' * 8,\
		 font = ("Arial", 20))
		self.text6 = self.canvas.create_text(350, 230, text = 'High Score',\
		 font = ("Arial", 20))
		self.point = self.canvas.create_polygon(10, 10, 15, 15, 10, 20)
		self.canvas.move(self.point, 260, 185 )
		self.tk.update()
		self.play = False
		self.exit = False
		self.help = False
		self.about = False
		self.high_score = False
		self.canvas.bind_all('<KeyPress-Up>', self.pointer)
		self.canvas.bind_all('<KeyPress-Down>', self.pointer)
		self.canvas.bind_all('<KeyPress-Return>', self.pointer)

	def pointer(self, evt):
		self.point_pos = self.canvas.coords(self.point)
		if evt.keysym == 'Up':
			if self.point_pos[1] > 210:
				self.canvas.move(self.point, 0, -30)
			else:
				self.canvas.move(self.point, 0, 120)
		elif evt.keysym == 'Down':
			if self.point_pos[1] < 300:
				self.canvas.move(self.point, 0, 30)
			else:
				self.canvas.move(self.point, 0, -120)
		elif evt.keysym == 'Return':
			if self.point_pos[1] < 300 and self.point_pos[1] >270:
				self.exit = True
			elif self.point_pos[1] < 210:
				self.play =True
			elif self.point_pos[1] < 240 and self.point_pos[1] > 210:
				self.high_score = True
			elif self.point_pos[1] < 270 and self.point_pos[1] > 240:
				self.help = True
			elif self.point_pos[1] < 330 and self.point_pos[1] > 300:
				self.about = True

	def clear(self):
		self.canvas.move(self.text1, 1000, 0)
		self.canvas.move(self.text2, 1000, 0)
		self.canvas.move(self.text3, 1000, 0)
		self.canvas.move(self.text4, 1000, 0)
		self.canvas.move(self.text5, 1000, 0)
		self.canvas.move(self.text6, 1000, 0)
		self.canvas.move(self.point, 1000, 0)
		self.tk.update()

	def come_back(self):
		self.canvas.move(self.text1, -1000, 0)
		self.canvas.move(self.text2, -1000, 0)
		self.canvas.move(self.text3, -1000, 0)
		self.canvas.move(self.text4, -1000, 0)
		self.canvas.move(self.text5, -1000, 0)
		self.canvas.move(self.text6, -1000, 0)
		self.canvas.move(self.point, -1000, 0)
		self.tk.update()

	def beg_loop(self):
		while 1:
			if self.exit == True or self.play == True:
				self.clear()
				break
			if self.help == True:
				self.clear()
				obj = Help(self.tk, self.canvas)
				self.help = False
				self.come_back()
				self.canvas.bind_all('<KeyPress-Return>', self.pointer)
			if self.high_score == True:
				self.clear()
				obj = High_Score(self.tk, self.canvas)
				self.high_score = False
				self.come_back()
				self.canvas.bind_all('<KeyPress-Return>', self.pointer)
			if self.about == True:
				self.clear()
				obj = About(self.tk, self.canvas)
				self.about = False
				self.come_back()
				self.canvas.bind_all('<KeyPress-Return>', self.pointer)
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.1)

class High_Score:
	def __init__(self, tk, canvas):
		self.canvas = canvas
		self.tk = tk
		self.id = self.canvas.create_text(350, 150, text = \
					'High Score', font = ("Times", 50))
		with open('data', 'r') as f:
			self.high_score = f.read(2)
		self.score_id = self.canvas.create_text(350, 215, text = \
			self.high_score, font = ("Snap ITC", 25))
		self.back_id = self.canvas.create_text(350, 260, text =\
		 'Back',font = ("Snap ITC", 20))
		self.back_point = self.canvas.create_polygon(10, 10, 15, 15, 10, 20)
		self.canvas.move(self.back_point, 300, 245 )
		self.back = False
		self.canvas.bind_all('<KeyPress-Return>', self.pointer)
		while 1:
			if self.back == True:
				break
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.1)

	def pointer(self, evt):
		self.canvas.move(self.id, 1000, 1000 )
		self.canvas.move(self.back_id, 1000, 1000 )
		self.canvas.move(self.score_id, 1000, 1000 )
		self.canvas.move(self.back_point, 1000, 1000 )
		self.back = True

class Help:
	def __init__(self, tk, canvas):
		self.canvas = canvas
		self.tk = tk
		self.id = self.canvas.create_text(350, 150, text = \
					'Help', font = ("Times", 50))
		self.content_id = self.canvas.create_text(350, 215, text = \
			'Use left and right arrows to control the paddle\n' + \
			'and make ball bounce to hit the targets.', font = ("Courier", 15))
		self.back_id = self.canvas.create_text(350, 260, text =\
		 'Back',font = ("Snap ITC", 20))
		self.back_point = self.canvas.create_polygon(10, 10, 15, 15, 10, 20)
		self.canvas.move(self.back_point, 300, 245 )
		self.back = False
		self.canvas.bind_all('<KeyPress-Return>', self.pointer)
		while 1:
			if self.back == True:
				break
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.1)

	def pointer(self, evt):
		self.canvas.move(self.id, 1000, 1000 )
		self.canvas.move(self.back_id, 1000, 1000 )
		self.canvas.move(self.content_id, 1000, 1000 )
		self.canvas.move(self.back_point, 1000, 1000 )
		self.back = True

class About:
	def __init__(self, tk, canvas):
		self.canvas = canvas
		self.tk = tk
		self.id = self.canvas.create_text(350, 150, text = \
					'About', font = ("Times", 50))
		self.content_id = self.canvas.create_text(350, 215, text = \
			'Credits: Rupesh Gyawali',\
			 font = ("Courier", 20))
		self.back_id = self.canvas.create_text(350, 260, text =\
		 'Back',font = ("Snap ITC", 20))
		self.back_point = self.canvas.create_polygon(10, 10, 15, 15, 10, 20)
		self.canvas.move(self.back_point, 300, 245 )
		self.back = False
		self.canvas.bind_all('<KeyPress-Return>', self.pointer)
		while 1:
			if self.back == True:
				break
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.1)

	def pointer(self, evt):
		self.canvas.move(self.id, 1000, 1000 )
		self.canvas.move(self.back_id, 1000, 1000 )
		self.canvas.move(self.content_id, 1000, 1000 )
		self.canvas.move(self.back_point, 1000, 1000 )
		self.back = True
