import random
import time


def print_with_delay(text):
	print(text)
	time.sleep(0.5)


def print_with_delay_2(text):
	print(text)
	time.sleep(1.1)


def intro():
	print_with_delay('\n------------ ********* ------------')
	print_with_delay('\n             WELCOME')
	print_with_delay('                TO')
	print_with_delay('           TIC-TAC-TOE!')
	print_with_delay('\n           ***********')
	print('              RULES')
	print('\nPlayers take turns putting their marks (X or O) in empty squares.')
	print('The first player to get 3 of their marks in a row')
	print('(up, down, across, or diagonally) is the winner.')
	print('When all 9 squares are full, the game is over.')
	print('If no player has 3 marks in a row, the game ends in a tie.')
	print('You will be playing against a computer.')
	print('\nATTENTION! Whoever plays as "X" goes first.')


def print_board(board):
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
	print('\n---------------------------------------')


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


# TODO: Unused player_symbol. Remove it as it is not used.
def player_move(board, player_symbol):
	while True:
		player_move_input = input('\nEnter your move (1-9): ')
		if player_move_input.isdigit() and 1 <= int(player_move_input) <= 9:
			move = int(player_move_input) - 1
			if 0 <= move <= 8 and board[move] == ' ':
				return move
			else:
				print_with_delay('Spot is taken! Try again and choose another spot!')
		else:
			print_with_delay('Please choose a number from 1 to 9.')


def computer_random_move(board):
	empty_cells = [i for i in range(9) if board[i] == ' ']
	if empty_cells:
		return random.choice(empty_cells)
	# TODO: It will be OK if you just leave out else and return None. Same effect, less lines
	else:
		return None


def computer_winning_move(board, computer_symbol):
	for i in range(9):
		if board[i] == ' ':
			board[i] = computer_symbol
			if check_winner(board, computer_symbol):
				return i
			board[i] = ' '
	# TODO: It will be OK if you just leave out return None. Same effect, less lines
	return None


def computer_blocking_move(board, player_symbol, computer_symbol):
	for i in range(9):
		if board[i] == ' ':
			board[i] = player_symbol
			if check_winner(board, player_symbol):
				board[i] = computer_symbol
				return i
			board[i] = ' '
	# TODO: It will be OK if you just leave out return None. Same effect, less lines.
	#  If nothing will be returned, the function's value will be None
	return None


def computer_move(board, computer_symbol, player_symbol):
	# TODO: As every return value means something else, I would split that in three separate functions.
	winning_move = computer_winning_move(board, computer_symbol)
	if winning_move:
		return winning_move

	blocking_move = computer_blocking_move(board, player_symbol, computer_symbol)
	if blocking_move:
		return blocking_move

	return computer_random_move(board)


def tic_tac_toe():
	while True:
		board = [' '] * 9
		player_symbol = input('\nChoose the symbol you want to play with (X or O): ').upper()
		if player_symbol in ('X', 'O'):
			computer_symbol = 'O' if player_symbol == 'X' else 'X'
			print_with_delay(f'You chose: {player_symbol}, computer will play as {computer_symbol}.')
		else:
			print_with_delay('\nOops, wrong input!')
			continue

		print_with_delay('\nAlright, let´s go!')
		current_player = 'X'

		while True:
			print("\n")
			print_board(board)

			if current_player == player_symbol:
				player_position = player_move(board, player_symbol)
				board[player_position] = player_symbol

				if check_winner(board, player_symbol):
					print_board(board)
					print_with_delay('\nYOU WON! YAY!')
					break

				current_player = computer_symbol

			else:
				print_with_delay_2(f'\nComputer´s move ({computer_symbol})...')
				computer_position = computer_move(board, computer_symbol, player_symbol)
				board[computer_position] = computer_symbol

				if check_winner(board, computer_symbol):
					print_board(board)
					print('You lost. Aww :´(')
					break

				current_player = player_symbol

			if ' ' not in board:
				print_board(board)
				print('\nIt´s a tie!')
				break

		play_again = input('\nDo you want to play again? (Y/N): ').upper()
		if play_again == "Y":
			print('\nGreat! Lets play again!')
			tic_tac_toe()
		else:
			print('\nBye! Have an awesome day!')
			break


intro()
tic_tac_toe()
