from buttons import Button

class Player:
    def __init__(self, type, color, highlight_color=None):
        self.type = type
        self.color = color
        self.highlight_color = highlight_color
        if highlight_color is None:
            self.highlight_color = color

    def make_move(self, game_board, event):
        done = False
        if self.type == "user":
            if event is None:
                return False
            for y in range(len(game_board)):
                for x in range(len(game_board[y])):
                    square = game_board[y][x]
                    if square.button.check_if_pressed(event.pos[0], event.pos[1]):
                        square.value = self.color
                        square.button.main_color = self.color
                        square.button.highlight_color = self.highlight_color
                        square.button.active = False
                        done = True

        if self.type == "ai":
            done = True

        return done
