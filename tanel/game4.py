import random

board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

coordinates = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

current_player = "X"
winner = None
game_on = True


# TODO: There is already a "board" variable in an outer scope.
#  Refrain from using the same name arguments for the function definitions.
def print_board(board):
	print(board[0] + "   :   " + board[1] + "   :   " + board[2])
	print(board[3] + "   :   " + board[4] + "   :   " + board[5])
	print(board[6] + "   :   " + board[7] + "   :   " + board[8])
	print("---------------")
	for row in coordinates:
		print(row)


def player_input(board):
	while True:
		chose_move = int(input("Enter coordinates 1-9: "))
		if 1 <= chose_move <= 9 and board[chose_move - 1] == "-":
			board[chose_move - 1] = current_player
		else:
			print("Try again, enter coordinates 1-9: ")
		break


def check_horizontal(board):
	global winner
	if board[0] == board[1] == board[2] and board[1] != "-":
		winner = board[0]
		return True
	elif board[3] == board[4] == board[5] and board[3] != "-":
		winner = board[3]
		return True
	elif board[6] == board[7] == board[8] and board[3] != "-":
		winner = board[6]
		return True
	elif board[0] == board[1] == board[2] and board[1] == "o":
		winner = board[0]
		return True
	elif board[3] == board[4] == board[5] and board[3] == "o":
		winner = board[3]
		return True
	elif board[6] == board[7] == board[8] and board[3] == "o":
		winner = board[6]
		return True
	else:
		return False


def check_row(board):
	global winner
	if board[0] == board[3] == board[6] and board[0] != "-":
		winner = board[0]
		return True
	elif board[1] == board[4] == board[7] and board[1] != "-":
		winner = board[1]
		return True
	elif board[2] == board[5] == board[8] and board[2] != "-":
		winner = board[1]
		return True
	elif board[0] == board[3] == board[6] and board[0] == "o":
		winner = board[0]
		return True
	elif board[1] == board[4] == board[7] and board[1] == "o":
		winner = board[1]
		return True
	elif board[2] == board[5] == board[8] and board[2] == "o":
		winner = board[1]
		return True
	else:
		return False


def check_diagonal(board):
	global winner
	if board[0] == board[4] == board[8] and board[0] != "-":
		winner = board[0]
		return True
	elif board[2] == board[4] == board[6] and board[2] != "-":
		winner = board[2]
		return True
	elif board[0] == board[4] == board[8] and board[0] == "o":
		winner = board[0]
		return True
	elif board[2] == board[4] == board[6] and board[2] == "o":
		winner = board[2]
		return True
	else:
		return False


def check_tie(board):
	global game_on
	if "-" not in board:
		print_board(board)
		print("It is a tie thank you for playing!")
		game_on = False


def check_win():
	global game_on
	if check_horizontal(board) or check_row(board) or check_diagonal(board):
		print_board(board)
		game_on = False
		print(f"winner is {winner}")
		exit("Thank you for playing")


def switch_player():
	global current_player
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"


def computer_player(board):
	while current_player == "O":
		position = random.randint(0, 8)
		if board[position] == "-":
			board[position] = "O"
			switch_player()


new_game = True
while new_game:
	print("Welcome to Tic-Tac-Toe game")
	start_game = input("Do you wanna play? (Y/N) :")

	# TODO: You ask the user to type in 'Y', but you evaluate 'y'.
	if start_game == "y":
		while game_on:
			print_board(board)
			player_input(board)
			check_win()
			check_tie(board)
			switch_player()
			computer_player(board)
			check_win()
			check_tie(board)



	else:
		exit("Have a nice day!")
