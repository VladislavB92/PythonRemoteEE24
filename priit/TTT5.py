import random

tic_tac_toe = [' '] * 9


# TODO: Separate functions and main game logic call in separate files.
def start_game():
	global tic_tac_toe
	for i in range(9):
		tic_tac_toe[i] = ' '


# TODO: Separate functions and main game logic call in separate files.
def who_goes_first():
	# TODO: No options to choose the player sign - X or O.
	if random.randint(0, 1) == 0:
		return "computer"
	else:
		return "player"


def print_game():
	global tic_tac_toe
	print("------------------------------------")
	print("")
	# TODO: DO NOT mix spaces and tabs for indentations. Only use TAB x4.
	# TODO: No validation for player signs. If I place "", the game crashes.
	print(
		" [{}] [{}] [{}]     [1] [2] [3]".format(
			tic_tac_toe[0], tic_tac_toe[1], tic_tac_toe[2])
	)
	# TODO: A better way to format a multi-line expression. Check the placement of the last bracket. Fixed.
	print(
		" [{}] [{}] [{}]     [4] [5] [6]".
		format(tic_tac_toe[3], tic_tac_toe[4], tic_tac_toe[5])
	)
	print(
		" [{}] [{}] [{}]     [7] [8] [9]".
		format(tic_tac_toe[6], tic_tac_toe[7], tic_tac_toe[8])
	)
	print("")


def machine_move():
	# TODO: DO NOT use globals!! Use arguments!
	global tic_tac_toe
	while True:
		r = random.randint(0, 8)
		if tic_tac_toe[r] == ' ':
			tic_tac_toe[r] = 'O'
			break


def check_end(p):
	# TODO: DO NOT use globals!! Use arguments!
	global tic_tac_toe
	t = tic_tac_toe

	# rows
	if t[0] == p and t[1] == p and t[2] == p:
		return True
	if t[3] == p and t[4] == p and t[5] == p:
		return True
	if t[6] == p and t[7] == p and t[8] == p:
		return True
	# columns
	if t[0] == p and t[3] == p and t[6] == p:
		return True
	if t[1] == p and t[4] == p and t[7] == p:
		return True
	if t[2] == p and t[5] == p and t[8] == p:
		return True
	# diags
	if t[0] == p and t[4] == p and t[8] == p:
		return True
	if t[2] == p and t[4] == p and t[6] == p:
		return True

	return False


def tie_conditions():
	# TODO: DO NOT use globals!! Use arguments!
	global tic_tac_toe
	for i in range(9):
		if tic_tac_toe[i] == ' ':
			return False
	return True


# TODO: Better to make function names imperative. Like "determine_first_player()".
who = who_goes_first()
while True:

	print("====WELCOME TO TIC-TAC-TOE====")
	start_game()

	if who == "computer":
		machine_move()
		print("Computer made the first move")
	else:
		print("You made the first move")
	while True:
		print_game()
		user_input = int(input("Place X in specific coordinate: "))

		if user_input < 1 or user_input > 9:
			print("Please insert number from 1 to 9")
			continue
		if tic_tac_toe[user_input - 1] != ' ':
			print("serious??")
			continue

		tic_tac_toe[user_input - 1] = 'X'
		if check_end('X'):
			print_game()
			print("player wins .. ")
			break
		machine_move()
		if check_end('O'):
			print_game()
			print("computer wins .. ")
			break
		if tie_conditions():
			print_game()
			print("TIE .. ")
			break

		continue

	user_choice_continue_game = input("Do you want to continue the game? y/n ")
	if user_choice_continue_game == "n":
		print("Bye!")
		break
