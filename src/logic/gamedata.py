import pickle
from pathlib import Path

def resolve_assets():
    cur_path = Path(__file__)
    while cur_path != Path('/') and Path('assets') not in cur_path.iterdir():
        cur_path = cur_path.parent()
    if Path('assets') in cur_path.iterdir():
        return cur_path / 'assets'
    else:
        raise FileNotFoundError('Assets folder could not be found')

class GameData:
    SAVE_PATH = resolve_assets()
    def __setattr__(self, name, obj):
        function_type = type(lambda x: x)
        if type(obj) in [type, function_type]:
            pass
        else:
            object.setattr(self, name, obj)

    def save(self):
        with open(SAVE_PATH, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def open():
        with open(SAVE_PATH, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def open_safe():
        if SAVE_PATH.exists():
            return GameData.open()
        else:
            return GameData()
