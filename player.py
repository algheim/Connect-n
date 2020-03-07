from buttons import Button

class Player:
    def __init__(self, type, color, highlight_color=None):
        self.type = type
        self.color = color
        self.highlight_color = highlight_color
        if highlight_color is None:
            self.highlight_color = color

    def make_move(self, game_board, event, gravity):
        if self.type == "user":
            done = self.get_user_move(game_board, event, gravity)
        if self.type == "ai":
            done = True
        return done

    def get_user_move(self, game_board, event, gravity):
        if event is None:
            return False
        for y in range(len(game_board)):
            for x in range(len(game_board[y])):
                square = game_board[y][x]
                if square.button.check_if_pressed(event.pos[0], event.pos[1]):
                    if gravity:
                        square = self.get_valid_square(game_board, x, y)
                    square.value = self.color
                    square.button.main_color = self.color
                    square.button.highlight_color = self.highlight_color
                    square.button.active = False
                    return True
        return False

    def get_valid_square(self, game_board, x, y):
        while y < len(game_board) - 1 and game_board[y + 1][x].value is None:
            y += 1

        return game_board[y][x]
