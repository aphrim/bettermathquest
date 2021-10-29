import pickle
from pathlib import Path

class GameData:
    SAVE_PATH = Path(__file__).parent().parent().parent() / 'assets'
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
