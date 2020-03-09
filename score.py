

def check_horizontal(game_board, goal):
    for row in game_board:
        c = 1
        prev_color = None
        for square in row:
            if square.value == prev_color and prev_color != None:
                c += 1
            else:
                c = 1
                prev_color = square.value

            if c == goal:
                return prev_color


def check_vertical(game_board, goal):
    if goal > len(game_board):
        return None

    for y in range(len(game_board) - goal + 1):
        for x in range(len(game_board[y])):
            if game_board[y][x].value is None:
                continue

            winner = True
            for i in range(1, goal):
                if game_board[y + i][x].value != game_board[y][x].value:
                    winner = False
            if winner:
                return game_board[y][x].value


def check_diag1(game_board, goal):
    for y in range(len(game_board) - goal + 1):
        for x in range(len(game_board[y]) - goal + 1):
            if game_board[y][x].value == None:
                continue

            winner = True
            for i in range(1, goal):
                if game_board[y + i][x + i].value != game_board[y][x]. value:
                    winner = False
            if winner:
                return game_board[y][x].value


def check_diag2(game_board, goal):
    if goal > len(game_board) or goal > len(game_board[0]):
        return None

    for y in range(len(game_board) - goal + 1):
        for x in range(goal - 1, len(game_board[y])):
            if game_board[y][x].value == None:
                continue

            winner = True
            for i in range(1, goal):
                if game_board[y + i][x - i].value != game_board[y][x]. value:
                    winner = False
            if winner:
                return game_board[y][x].value

def check_tie(game_board):
    tie = True
    for row in game_board:
        for square in row:
            if square.value == None:
                tie = False

    return tie


def check_winner(game_board, goal):
    if check_horizontal(game_board, goal) is not None:
        return check_horizontal(game_board, goal)
    if check_vertical(game_board, goal) is not None:
        return check_vertical(game_board, goal)
    if check_diag1(game_board, goal) is not None:
        return check_diag1(game_board, goal)
    if check_diag2(game_board, goal) is not None:
        return check_diag2(game_board, goal)
    if check_tie(game_board):
        return "tie"
    return None


def get_score(game_board, player, players, goal):
    winner = check_winner(game_board, goal)
    if winner == player.color:
        return 10000
    if winner == "tie":
        return 0
    if winner is not None:
        return -10000

    return 1
