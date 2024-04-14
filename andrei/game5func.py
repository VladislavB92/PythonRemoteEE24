def win_check(player_moves_history):
	win_conditions = [
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
		{1, 4, 7},
		{2, 5, 8},
		{3, 6, 9},
		{1, 5, 9},
		{7, 5, 3},
	]
	for winset in win_conditions:
		if winset.issubset(player_moves_history):
			return True


def get_coordinates(user_input):
	tic_coordinates = {
		1: "00",
		2: "01",
		3: "02",
		4: "10",
		5: "11",
		6: "12",
		7: "20",
		8: "21",
		9: "22",
	}
	input_coordinates = tic_coordinates.get(user_input)
	x, y = int(input_coordinates[0]), int(input_coordinates[1])
	return x, y
