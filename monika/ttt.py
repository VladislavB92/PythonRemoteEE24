print("===WELCOME TO TIC-TAC-TOE===")
print("")
print("Game table")
print(row)


def __init__(self):
	self.tic_tac_toe = [
		["", "", ""],
		["", "", ""],
		["", "", ""]
	]

	self.coordinates = [
		["1", "2", "3"],
		["4", "5", "6"],
		["7", "8", "9"]
	]


def display_board(self):
	print("====WELCOME TO TIC-TAC-TOE====")
	print("Game Table")
	for row in self.tic_tac_toe:
		print(row)
	print("\n------------------------------------\n")
	for row in self.coordinates:
		print(row)
	print()


def place_symbol(self, symbol, position):
	for row in range(3):
		for col in range(3):
			if self.coordinates[row][col] == str(position):
				if self.tic_tac_toe[row][col] == "":
					self.tic_tac_toe[row][col] = symbol
					return True
				else:
					return False


def check_winner(self):
	# Check rows, columns, and diagonals
	for i in range(3):
		if self.tic_tac_toe[i][0] == self.tic_tac_toe[i][1] == self.tic_tac_toe[i][2] != "":
			return True
		if self.tic_tac_toe[0][i] == self.tic_tac_toe[1][i] == self.tic_tac_toe[2][i] != "":
			return True
	if self.tic_tac_toe[0][0] == self.tic_tac_toe[1][1] == self.tic_tac_toe[2][2] != "":
		return True
	if self.tic_tac_toe[0][2] == self.tic_tac_toe[1][1] == self.tic_tac_toe[2][0] != "":
		return True
	return False


# Main game loop
tic_tac_toe_game = TicTacToe()
continue_game = True

while continue_game:
	tic_tac_toe_game.display_board()

	user_symbol = "X"  # Alternatively, switch between X and O
	user_position = int(input(f"Place {user_symbol} in a specific coordinate: "))
	if not tic_tac_toe_game.place_symbol(user_symbol, user_position):
		print("Invalid move! Cell is already filled.")
		continue

	if tic_tac_toe_game.check_winner():
		print("Congratulations! Player", user_symbol, "wins!")
		continue_game = False
	else:
		user_choice_continue_game = input("Do you want to continue the game? (y/n): ")
		if user_choice_continue_game.lower() == "n":
			continue_game = False
			print("Bye!")
