import random, sys
print("BATU"," KERTAS" , "AIR")

win = 0
lose = 0
ties = 0

while True:
	print("Result: {} Menang, {} Kalah, {} Seri".format(win,lose,ties))

	while True:
		print("Enter your move: (b)atu, (k)ertas, (g)unting or (q)uit")

		playerMove = input("tulis Sini ...")
		if playerMove == 'q':
			sys.exit()

		if playerMove == 'b' or playerMove == 'k' or playerMove == 'g':
			break


		print('Type one of b, k , g or q.')

	if playerMove == 'b':
		print("Batu lawan ... ")
	
	elif playerMove == 'k':
		print("Kertas lawan ... ")

	elif playerMove == 'g':
		print("Gunting lawan ... ")

	#SetupSystem
	randomNumber = random.randint(1,3)

	if randomNumber == 1:
		computerMove = 'b'
		print("Batu")

	elif randomNumber == 2:
		computerMove = 'k'
		print("Kertas")

	elif randomNumber == 3:
		computerMove = 'g'
		print("Gunting")

	#SetupGame
	if playerMove == computerMove:
		print("Keputusan SERI!")
		ties = ties + 1

	elif playerMove == 'b' and computerMove == 'g':
		print("Tahniah kamu MENANG ")
		win = win + 1

	elif playerMove == 'k' and computerMove == 'b':
		print("Tahniah kamu MENANG ")
		win = win + 1

	elif playerMove == 'g' and computerMove == 'k':
		print("Tahniah kamu MENANG! ")
		win = win + 1

	elif playerMove == 'b' and computerMove == 'k':
		print("Kamu TEWAS! ")
		lose = lose + 1

	elif playerMove == 'k' and computerMove == 'g':
		print("Kamu TEWAS! ")
		lose = lose + 1

	elif playerMove == 'g' and computerMove == 'b':
		print("Kamu TEWAS! ")
		lose = lose + 1
