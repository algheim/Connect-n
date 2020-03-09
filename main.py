import pygame as p
from game import Game
from player import Player

# ------------options-------------
SCREEN_LENGTH = 600
SCREEN_HEIGHT = 600
BOARD_LENGTH = 7
BOARD_HEIGHT = 5
GOAL = 4
GRAVITY = True
DEPTH = 4
# ------------colors--------------
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# --------------------------------

win = p.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
players = [Player("user", RED), Player("ai", GREEN)]
game = Game(players, BOARD_LENGTH, BOARD_HEIGHT, GOAL, GRAVITY, DEPTH, win)

while True:
    game.update_event()
    game.update_game_board()
    game.check_winner()
    game.draw()
    game.end_game()
