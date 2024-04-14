import random

board = [" "] * 10
player = "x"
computer = "o"
game = True

print("====WELCOME TO TIC-TAC-TOE====")


def display_board(board):
	print(f"{board[1]} | {board[2]} | {board[3]}")
	print("-" * 10)
	print(f"{board[4]} | {board[5]} | {board[6]}")
	print("-" * 10)
	print(f"{board[7]} | {board[8]} | {board[9]}")

	print("_" * 10)


def check_win():
	if board[1] == board[2] == board[3] and board[1] != " ":
		return True
	elif board[4] == board[5] == board[6] and board[4] != " ":
		return True
	elif board[7] == board[8] == board[9] and board[7] != " ":
		return True
	elif board[1] == board[4] == board[7] and board[1] != " ":
		return True
	elif board[2] == board[5] == board[8] and board[2] != " ":
		return True
	elif board[3] == board[6] == board[9] and board[3] != " ":
		return True
	elif board[1] == board[5] == board[9] and board[1] != " ":
		return True
	elif board[3] == board[5] == board[7] and board[3] != " ":
		return True
	else:
		return False


def check_draw():
	if board.count(" ") < 2:
		return True
	else:
		return False


def is_available(inp):
	return True if board[inp] == " " else False


def insert(letter, inp, check_replay):
	if is_available(inp):
		board[inp] = letter
		display_board(board)
		if check_win():
			if letter == "x":
				print("Player wins!")
				exit()
			else:
				print("Computer wins!")
				exit()
		if check_draw():
			print("Draw!")
			exit()

	else:
		if letter == "o":
			inp = int(input("Position already occupied. Try again! "))
		else:
			inp = random.randint(1, 9)
		insert(letter, inp)


def player_input(letter):
	inp = int(input("Enter the position to insert: "))
	insert(letter, inp)


def computer_input(letter):
	inp = random.randint(1, 9)
	if insert(letter, inp):
		return


# main loop

while game:
	check_win()
	display_board(board)
	player_input(player)
	computer_input(computer)
