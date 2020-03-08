from checkwinner import check_winner
from score import get_score


class Ai:
    def __init__(self, game_board, gravity, goal, players, depth):
        self.game_board = game_board
        self.gravity = gravity
        self.goal = goal
        self.players = players
        self.depth = depth
        self.player = None

    def get_possible_moves(self):
        possible_moves = []
        for y in range(len(self.game_board)):
            for x in range(len(self.game_board[y])):
                if self.game_board[y][x].value is None:
                    if not self.gravity:
                        possible_moves.append((x, y))
                    else:
                        if (y == len(self.game_board) - 1 or
                        self.game_board[y + 1][x].value is not None):
                            possible_moves.append((x, y))

        return possible_moves

    def get_best_move(self, player):
        best_score = -10000
        best_move = None
        for move in self.get_possible_moves():
            self.game_board[move[1]][move[0]].value = player.color
            score = -self.two_player_min_max(self.change_turn(self.player), self.depth)
            self.game_board[move[1]][move[0]].value = None
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def two_player_min_max(self, player, depth):
        score = get_score(self.game_board, player, self.goal)
        if score == 10000 or score == -10000 or score == 0 or depth == 0:
            return score

        best_score = -100000
        for move in self.get_possible_moves():
            self.game_board[move[1]][move[0]].value = player.color
            score = -self.two_player_min_max(self.change_turn(player), depth - 1)
            self.game_board[move[1]][move[0]].value = None
            best_score = max(score, best_score)

        return best_score

    def change_turn(self, player):
        if player == self.players[0]:
            return self.players[1]
        return self.players[0]


        index = 0
        for i in range(len(self.players)):
            if self.players[i] == player:
                index = i
                break

        if index + 1 == len(self.players):
            return self.players[0]
        return self.players[index + 1]
