import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.running = True
        self.screen = None
        self.pressed_keys = []

        self.init_game()

    def game_loop(self):
        self.pressed_keys = pygame.key.get_pressed()
        print("Game Loop Start")

    def render_loop(self):
        print("Render Loop Start")

    def poll_events(self):
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                return False

        pygame.display.flip()
        return True

    def init_game(self):
        print("Game Init Start")
        pygame.init()
        screen = pygame.display.set_mode((400,500)) 
        self.screen = screen

game = Game()

while game.running:
    if not game.poll_events():
        pygame.quit()
        break
    game.game_loop()
    game.render_loop()
