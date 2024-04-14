import random
from game5func import win_check, get_coordinates

print("====WELCOME TO TIC-TAC-TOE====")

new_game = True
while new_game:
	print("")
	start_game = input('Press any key to start a new game, (e) will exit the game: ')
	if start_game == 'e':
		exit("Bye!")

	tic_tac_toe = [
		["-", "-", "-"],
		["-", "-", "-"],
		["-", "-", "-"],
	]

	coordinates = [
		["1", "2", "3"],
		["4", "5", "6"],
		["7", "8", "9"],
	]

	check_coord = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	x_moves = set()
	o_moves = set()

	game = True

	while game:
		print("Game table")
		for row in tic_tac_toe:
			print(row)
		print("")
		print("------------------------------------")
		print("")
		for cell in coordinates:
			print(cell)
		print("")

		x_input = None
		while x_input not in check_coord:
			try:
				x_input = int(input("Place an X (choose coordinates): "))
			except ValueError:
				print("Enter valid coordinate")
		x, y = get_coordinates(x_input)
		tic_tac_toe[x][y] = "X"
		coordinates[x][y] = "X"
		check_coord.remove(x_input)
		x_moves.add(x_input)
		for row in tic_tac_toe:
			print(row)
		if win_check(x_moves):
			print("X WINS!")
			break

		if len(check_coord) == 0:
			print("It's a tie!")
			break

		print("O move:")
		o_input = int(random.choice(check_coord))
		x, y = get_coordinates(o_input)
		tic_tac_toe[x][y] = "O"
		coordinates[x][y] = "O"
		check_coord.remove(o_input)
		o_moves.add(o_input)

		for row in tic_tac_toe:
			print(row)

		if win_check(o_moves):
			print("O Wins!")
			break
