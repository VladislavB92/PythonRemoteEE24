tic_tac_toe = [
	["", "", ""],
	["", "", ""],
	["", "", ""],
]  # 2d list

coordinates = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"],
]

# What do we need?
# What is the game? What are the rules.
# What kind of users we will have? Two players, who will play the game in turns.

# 1. Input
# 2. Position of the input
# 3. Conditions (who wins, who looses, draw, what determines the winner?)
# 4. Re-playability
# Should include extra: dictionary, tuple, set, functions/methods, and classes/objects

game = True

while game:
	print("====WELCOME TO TIC-TAC-TOE====")
	print("")
	print("Game table")
	for row in tic_tac_toe:
		print(row)
	print("")
	print("------------------------------------")
	print("")
	for cell in coordinates:
		print(cell)
	print("")

	user_x = int(input("Place X in specific coordinate: "))

	user_choice_continue_game = input("Do you want to continue the game? y/n ")
	if user_choice_continue_game == "y":
		game = True
	elif user_choice_continue_game == "n":
		game = False
		print("Bye!")

