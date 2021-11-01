import pygame

def game_loop(self):
    self.pressed_keys = pygame.key.get_pressed()
    self.game_map.game_loop(self)
    # print("Game Loop Start")
