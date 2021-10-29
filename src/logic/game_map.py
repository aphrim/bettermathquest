from dataclasses import dataclass
from typing import *

class GameMap:
    def __init__(self, game_map):
        self.game_map = [PosSlice([x]) if type(x) != PosSlice else x for y in game_map for x in y]  # Confusing. Rewrite.

    @staticmethod
    def load_from_file(filename):
        with open(filename) as f:
            # Do stuff here.
            pass

class Room:
    def __init__(self, moveable_locations):
        self.moveable_locations = moveable_locations   # How to specify so that decimals work.
        self.player_pos = None

    def set_player_pos(self, x, y):
        pass
        # Will prevent illegal moves.

@dataclass
class PosSlice:  # Represents all rooms on the same x,y coordinates, including underground rooms
    self.rooms: List[Rooms]
    self.level: int = -1
