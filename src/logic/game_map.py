from dataclasses import dataclass
from pygame import *
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
        ks = game.pressed_keys
        delta = [0, 0]
        if ks[K_UP]:
            delta[1] = -GameMap.VERTICAL_STEP
        if ks[K_LEFT]:
            delta[0] = -GameMap.HORIZONTAL_STEP
        if ks[K_DOWN]:
            delta[1] = GameMap.VERTICAL_STEP
        if ks[K_RIGHT]:
            delta[0] = GameMap.HORIZONTAL_STEP
        new_cposx, new_cposy = self.cposx, self.cposy
        new_cposx += delta[0]
        new_cposy += delta[1]
        if self.current_room.can_move(new_cposx, new_cposy):
            self.cposx, self.cposy = new_cposx, new_cposy
        outside = self.current_room.outside(self.cposx, self.cposy)
        if outside:
            rdx, rdy = outside
            self.posx += rdx
            self.posy += rdy


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

    @staticmethod
    def make_sample_tile():
        return Tile('none', 10, 10, True)

class Room:
    def __init__(self, tiles):
        self.tiles = tiles
        self.width = len(tiles) * Tile.WIDTH
        self.height = len(tiles[0]) * Tile.HEIGHT        # Height

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def can_move(self, x, y):
        int_pos = (int(x), int(y))
        try:
            return self.get_tile(*int_pos).accessable
        except:
            return False
        pass

    def outside(self, x, y):
        if x > self.width:
            return (1, 0)
        elif x < 0:
            return (-1, 0)
        elif y > self.height:
            return (0, 1)
        elif y < 0:
            return (0, -1)
        else:
            return False

    @staticmethod
    def make_sample_room():
        return Room([[Tile.make_sample_tile() for x in range(10)] for y in range(10)])