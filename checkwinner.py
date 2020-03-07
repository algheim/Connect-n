
def check_horizontal(game_board, goal):
    for row in game_board:
        c = 0
        color = None
        for square in row:
            if square.value == color:
                c += 1
            else:
                c = 0
                color = None

            if c == goal:
                return color


def check_winner(game_board, goal):
    return check_horizontal(game_board, goal)
