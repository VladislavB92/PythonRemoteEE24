print("====WELCOME TO TIC-TAC-TOE====")
print("")
print("Game table")

board = [
	["-", "-", "-"],
	["-", "-", "-"],
	["-", "-", "-"],
]  # 2d list

coordinates = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"],
]


# TODO: There is already a "board" variable in an outer scope.
#  Refrain from using the same name arguments for the function definitions.
def print_board(board):
	print("|", board[0], "|", board[1], "|", board[2], "|")
	print("|", board[3], "|", board[4], "|", board[5], "|")
	print("|", board[6], "|", board[7], "|", board[8], "|")


def check_winner(board):
	win_combinations = [
		[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
		[0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
		[0, 4, 8], [2, 4, 6]  # Diagonal
	]
	for combination in win_combinations:
		if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
			return True
	return False


def update_board(board, position, symbol):
	board[position - 1] = symbol


def play_game():
	while True:
		board = [" "] * 9
		symbols = ["X", "O"]
		count = 0

		while True:
			print_board(board)
			symbol = symbols[count % 2]
			position = player_move(board, symbol)
			update_board(board, position, symbol)
			if check_winner(board):
				print_board(board)
				print(f"Player {symbol} wins!")
				break
			count += 1
			if count == 9:
				print_board(board)
				print("It's a draw!")
				break

		play_again_input = input("Do you want to play again? (y/n): ")
		if play_again_input.lower() != "y":
			break


def player_move(board, symbol):
	while True:
		try:
			position = int(input(f"Player {symbol}, choose your position (1-9): "))
			if 1 <= position <= 9 and board[position - 1] == " ":
				return position
			else:
				print("Invalid position! Please choose an empty position.")
		except ValueError:
			print("Invalid input! Please enter a number.")


# TODO: You can move all functions to another file and just leave this function call in a separate file.
play_game()
print("Bye!")
