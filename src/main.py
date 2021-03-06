import pygame
from pygame.locals import *
from renderloop import render_loop
from gameloop import game_loop
from logic.game_map import GameMap, Room

class Game:
    def __init__(self):
        self.running = True
        self.screen = None
        self.pressed_keys = []
        self.active_room = None
        self.game_map = GameMap([[Room.make_sample_room() for y in range(10)] for x in range(10)])


        self.init_game()


    def poll_events(self):
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                return False

        pygame.display.flip()
        return True

    def init_game(self):
        pygame.init()
        screen = pygame.display.set_mode((400,500)) 
        self.screen = screen

game = Game()

while game.running:
    if not game.poll_events():
        pygame.quit()
        break
    game_loop(game)
    render_loop(game)
