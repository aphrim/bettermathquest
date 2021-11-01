import pickle
from pathlib import Path

def resolve_assets():
    cur_path = Path(__file__).parent
    test_path = lambda p: (p / 'assets').exists()
    while cur_path != Path('/') and not test_path(cur_path):
        print(cur_path, (cur_path/'assets').exists())
        cur_path = cur_path.parent
    if test_path(cur_path):
        return cur_path / 'assets'
    else:
        raise FileNotFoundError('Assets folder could not be found')

class GameData:                         # TODO: Continue working on this
    SAVE_PATH = resolve_assets()
    initializations = {}
    def __init__(self, name='default'):
        self.name = name
        initializations.append(self)

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
