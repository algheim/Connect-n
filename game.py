import pygame as p
from buttons import Button
from square import Square

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self, players, board_length, board_height, gravity, win):
        self.players = players
        self.board_length = board_length
        self.board_height = board_height
        self.gravity = gravity
        self.win = win
        self.win_size = win.get_size()
        self.tile_length = int(self.win_size[0] * 0.9 / board_length)
        self.tile_height = int(self.win_size[1] * 0.9 / board_height)
        self.length_offset = int(self.win_size[0] * 0.05)
        self.height_offset = int(self.win_size[1] * 0.05)
        self.game_board = self.get_game_board()
        self.event = None
        self.turn = 0

    def get_game_board(self):
        game_board = []
        for y in range(self.board_height):
            game_board.append([])
            for x in range(self.board_length):
                button = Button(self.length_offset + self.tile_length * x,
                                self.height_offset + self.tile_height * y,
                                self.tile_length, self.tile_height)
                button.highlight_color = (230, 230, 230)
                game_board[y].append(Square(None, button))

        return game_board

    def update_event(self):
        self.event = None
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()

            if event.type == p.MOUSEBUTTONDOWN:
                self.event = event

    def update_game_board(self):
        done = self.players[self.turn].make_move(self.game_board, self.event)
        if done:
            self.change_turn()

    def change_turn(self):
        self.turn += 1
        if self.turn == len(self.players):
            self.turn = 0

    def draw(self):
        self.win.fill(BLACK)
        for y in range(self.board_height):
            for x in range(self.board_length):
                self.game_board[y][x].button.update_highlight()
                self.game_board[y][x].button.draw(self.win)

        p.display.update()
