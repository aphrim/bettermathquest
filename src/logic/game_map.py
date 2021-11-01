from dataclasses import dataclass
from typing import *

class GameMap:
    VERTICAL_STEP = 1
    HORIZONTAL_STEP = 1

    def __init__(self, game_map, pos=(0, 0), cpos=(0, 0)):
        self.game_map = game_map
        self.posx, self.posy = pos
        self.cposx, self.cposy = cpos

    @property
    def current_room(self):
        return self.game_map[self.posy][self.posx]

    def game_loop(self, game):
        ks = self.game.pressed_keys
        delta = [0, 0]
        if 'w' in ks:
            delta[1] = -VERTICAL_STEP
        if 'a' in ks:
            delta[0] = -HORIZONTAL_STEP
        if 's' in ks:
            delta[1] = VERTICAL_STEP
        if 'd' in ks:
            delta[0] = HORIZONTAL_STEP
        new_cposx, new_cposy = self.cposx, self.cposy
        self.new_cposx += delta[0]
        self.new_cposy += delta[1]
        if self.current_room.can_move(new_cposx, new_cposy):
            self.cposx, self.cposy = self.new_cposx, self.new_cposy


    @staticmethod
    def load_from_file(filename):
        with open(filename) as f:
            pass

class Tile:        # Fix in the future
    HEIGHT = 5
    WIDTH = 5
    def __init__(self, texture, x, y, accessable):   # x and y are NOT the actual coordinates; they are its coordinates in terms of tiles
        self.texture = texture
        self.x, self.y = x, y
        self._x, self._y = x * Tile.WIDTH, y * Tile.HEIGHT
        self.accessable = accessable

class Room:
    def __init__(self, tiles):
        self.tiles = tiles
        self.length = len(tiles) * Tile.LENGTH
        self.width = len(tiles[0]) * Tile.WIDTH

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def can_move(self, x, y):
        int_pos = (int(x), int(y))
        return get_tile(*int_pos).accessable
