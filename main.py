import pygame as p
from game import Game
from player import Player

RED = (255, 0 ,0)
GREEN = (0, 255, 0)

SCREEN_LENGTH = 500
SCREEN_HEIGHT = 700
win = p.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
players = [Player("user", RED), Player("user", GREEN)]
game = Game(players, 3, 4, 3, False, win)

while True:
    game.update_event()
    game.update_game_board()
    game.check_winner()

    game.draw()
