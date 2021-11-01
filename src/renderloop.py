from pygame import *


def render_loop(self):
    self.screen.fill(((0,0,0)))
    playerPosX = self.game_map.cposx
    playerPosY = self.game_map.cposy
    print(playerPosX, playerPosY)
    self.screen.set_at((playerPosX, playerPosY), Color(255, 255, 255))
    # print("Render Loop Start")
