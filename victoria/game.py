import random
import time


# TODO: Better to split the functions in separate files
#  and just have a main game.py file where you call the main game functionality.
def print_with_delay(text):
	print(text)
	time.sleep(0.5)


def print_with_delay_longer(text):
	print(text)
	time.sleep(1.0)


def intro():
	print_with_delay("\nWelcome to magical world of Tic-Tac-Toe!")
	print_with_delay(" Here are some hints how to play it.")
	print_with_delay("  Players take turns placing their marks (X or O) in empty squares.")
	print_with_delay("   The first player to get 3 of their marks in a row wins!")
	print_with_delay("  You can win horizontally, vertically, or diagonally.")
	print_with_delay("If all 9 squares are filled without a winner, it´s a tie.")


def print_board(board):
	print('    ============================')
	print('            1 | 2 | 3')
	print('           ---|---|---')
	print('            4 | 5 | 6')
	print('           ---|---|---')
	print('            7 | 8 | 9')
	print()
	print('            ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
	print('           ---|---|---')
	print('            ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
	print('           ---|---|---')
	print('            ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
	print('    ============================')


def check_winner(board, player):
	winning_combinations = [
		[0, 1, 2], [3, 4, 5], [6, 7, 8],
		[0, 3, 6], [1, 4, 7], [2, 5, 8],
		[0, 4, 8], [2, 4, 6]
	]
	for combo in winning_combinations:
		if all(board[i] == player for i in combo):
			return True
	return False


# TODO: Unused computer_player argument in the function. That is why it is in grey. You can remove it freely.
def imaginary_friends_move(board, computer_player):
	empty_spots = [i for i in range(9) if board[i] == " "]
	if empty_spots:
		return random.choice(empty_spots)
	return None


# TODO: Unused player argument in the function. That is why it is in grey. You can remove it freely.
def player_move(board, player):
	while True:
		try:
			move = int(input("Enter your move (1-9): ")) - 1
			if 0 <= move <= 8 and board[move] == " ":
				return move
			else:
				print("Spot is taken! Try again and choose another.")
		except ValueError:
			print("Not quite correct! Please choose a number from 1 to 9.")


def tic_tac_toe():
	print("\n")
	print_with_delay("       =======================TIC-+TAC+-TOE=========================")
	print_with_delay("       -------------------------------------------------------------")
	board = [" "] * 9

	print("\n")

	while True:
		player_symbol = input("Choose the symbol for yourself (x or o): ").lower()
		imaginary_friends_symbol = "x" if player_symbol == "o" else "o"
		if player_symbol in ["x", "o"]:
			# TODO: A better way how to format the long line (brackets on separate lines from the f-string.
			print_with_delay_longer(
				f"\nYou play as {player_symbol}, imaginary friend plays as {imaginary_friends_symbol}"
			)
			break

		else:
			print("\nUps, something went wrong! Let's try once more! Choose between 'x' or 'o'.")

	print_with_delay("\nAll set!")
	print_with_delay("Read! Steady! GO!")

	while True:
		print("\n")
		print_board(board)

		player_position = player_move(board, player_symbol)
		board[player_position] = player_symbol

		if check_winner(board, player_symbol):
			print_board(board)

			print("\nYou are the WINNER!")
			break

		if " " not in board:
			print_board(board)
			print("\n")
			print("It´s a tie!")
			break

		print_with_delay_longer("\nImaginary friend´s move...")

		imaginary_friends_position = imaginary_friends_move(board, imaginary_friends_symbol)
		board[imaginary_friends_position] = imaginary_friends_symbol

		if check_winner(board, imaginary_friends_symbol):
			print_board(board)
			print("Your imaginary friend won!")
			break

	play_again = input("\nDo you want to play again? (yes/no): ").lower()
	if play_again == "yes":
		print("\nLet´s play another round!")
		# TODO: Better to start the loop from the beginning with a clear board rather that call the function insided itself.
		tic_tac_toe()
	# TODO: If I type anything except no, it still will quite the game.
	#  Better to elso evaluate with elif == "no".
	else:
		print("\nBye! See you soon!")
		print("\n")


intro()
tic_tac_toe()
