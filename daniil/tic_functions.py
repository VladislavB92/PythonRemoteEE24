def win_check(player_moves_history):
    win_conditions = [
        {"1", "2", "3"},
        {"4", "5", "6"},
        {"7", "8", "9"},
        {"1", "4", "7"},
        {"2", "5", "8"},
        {"3", "6", "9"},
        {"1", "5", "9"},
        {"3", "5", "7"}
    ]
    for win_set in win_conditions:
        if win_set.issubset(player_moves_history):
            return True


def move_check(moves_history, unused_cells):
    for element in unused_cells:
        moves_history.add(element)
        if win_check(moves_history):
            moves_history.remove(element)
            return element
        moves_history.remove(element)
