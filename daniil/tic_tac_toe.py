import random
from time import sleep
from tic_classes import Board
from tic_functions import win_check, move_check

print("====WELCOME TO TIC-TAC-TOE====")

new_game = True
while new_game:
	print("")
	start_game = input("Press any key to start a new game. (e) will exit the game: ")
	if start_game == "e":
		exit("Bye!")

	# TODO: Correct way how to format parameters.
	game_board = Board(
		"-", "-", "-",
		"-", "-", "-",
		"-", "-", "-"
	)

	# TODO: Correct way how to format parameters.
	game_coordinates = Board(
		"1", "2", "3",
		"4", "5", "6",
		"7", "8", "9"
	)

	possible_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	x_moves = set()
	o_moves = set()

	game = True
	while game:
		print("Game table")
		game_board.board_output()
		print("")
		print("------------------------------------")
		print("")
		game_coordinates.board_output()

		x_input = None

		# TODO: Could be nice if the user could choose the playing symbol - X or 0.
		while x_input not in possible_moves:
			x_input = input("Choose coordinates(1-9): ")
		game_board.board_input(x_input, "X")
		game_coordinates.board_input(x_input, "X")
		game_board.board_output()
		possible_moves.remove(x_input)
		x_moves.add(x_input)
		if win_check(x_moves):
			print("X WINS!")
			break

		if len(possible_moves) == 0:
			print("TIE!")
			break

		print("O move:")
		sleep(1)

		# TODO: You can just check if move_check(o_moves, possible_moves):
		if move_check(o_moves, possible_moves) is not None:
			o_input = move_check(o_moves, possible_moves)

		# TODO: A better way how to format long evaluations.
		# TODO: You can just check elif not move_check(o_moves, possible_moves)
		# 				and move_check(x_moves, possible_moves)
		elif (
				move_check(o_moves, possible_moves) is None
				and move_check(x_moves, possible_moves) is not None
		):
			o_input = move_check(x_moves, possible_moves)
		else:
			o_input = random.choice(possible_moves)
		game_board.board_input(o_input, "O")
		game_coordinates.board_input(o_input, "O")
		game_board.board_output()
		possible_moves.remove(o_input)
		o_moves.add(o_input)
		if win_check(o_moves):
			print("O WINS!")
			break
