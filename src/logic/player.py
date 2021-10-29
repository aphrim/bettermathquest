from dataclasses import dataclass

@dataclass
class PlayerInfo:    # What should be known at the start of the game
    appearance: str      # How the character looks (e.g. girl/boy)

@dataclass
class Player:
    player_info: PlayerInfo
    skills: list = []
    items: list = []
    quests: list = []
