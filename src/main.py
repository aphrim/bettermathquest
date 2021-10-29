import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        self.running = True
        self.screen = self.init_game()

    def game_loop():
        print("Game Loop Start")

    def render_loop():
        print("Render Loop Start")

    def poll_events():
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                return False

        pygame.display.flip()
        return True

    def init_game():
        print("Game Init Start")
        pygame.init()
        screen = pygame.display.set_mode((400,500)) 
        screen


game = Game()

while game.running:
    if ( not game.poll_events() ):
        pygame.quit()
        break
    game.game_loop()
    game.render_loop()
