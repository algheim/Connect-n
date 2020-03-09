from checkwinner import check_winner


def check_horizontal(game_board, player, players):
    player_score = 0
    opponent_score = 0
    for p in players:
        for y in range(len(game_board)):
            c = 0
            for x in range(len(game_board[y])):
                if game_board[y][x].value == p.color:
                    c += 1
                else:
                    if p == player:
                        player_score += c ** 2
                    else:
                        opponent_score += c ** 2
                    c = 0

    player_score -= opponent_score
    return player_score
    

def get_score(game_board, player, players, goal):
    winner = check_winner(game_board, goal)
    if winner == player.color:
        return 10000
    if winner == "tie":
        return 0
    if winner is not None:
        return -10000

    score = check_horizontal(game_board, player, players)
    if score == 0:
        score = 1
    return score
