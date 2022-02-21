
import _main_
import begin
import over

try:
	f = open('data')
except FileNotFoundError:
	with open('data', 'w') as f:
		f.write('00')
else:
	f.close()

bounce_game = _main_.Game()

def play_game(game):
	global paddle
	global ball
	global target
	paddle = _main_.Paddle(game.canvas)
	ball = _main_.Ball(game.canvas, paddle)
	target = _main_.Target(game.canvas, ball)
	game.main_loop(ball, paddle, target)

gm_start = begin.Game_Start(bounce_game.tk, bounce_game.canvas)
gm_start.beg_loop()

while 1:
	if gm_start.exit == True:
		break
	play_game(bounce_game)
	if target.complete == True:
		gm_complete = over.Game_Complete(bounce_game.tk, bounce_game.canvas, target)
		gm_complete.over_loop()
		ball.canvas.move(ball.id, 1000, 1000)
		paddle.canvas.move(paddle.id, 1000, 1000)
		for i in target.id_list:
			target.canvas.move(i, 1000, 1000)
		if gm_complete.restart == True:
			continue
		if gm_complete.exit == True:
			break
	else:
	 	gm_over = over.Game_Over(bounce_game.tk, bounce_game.canvas, target)
	 	gm_over.over_loop()
	 	ball.canvas.move(ball.id, 1000, 1000)
	 	paddle.canvas.move(paddle.id, 1000, 1000)
	 	for i in target.id_list:
	 		target.canvas.move(i, 1000, 1000)
	 	if gm_over.restart == True:
	 		continue
	 	if gm_over.exit == True:
	 		break
