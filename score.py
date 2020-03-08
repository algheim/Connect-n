from checkwinner import check_winner

def get_score(game_board, player, goal):
    winner = check_winner(game_board, goal)
    if winner == player.color:
        return 10000
    if winner == "tie":
        return 0
    if winner is not None:
        return -10000

    return 1
