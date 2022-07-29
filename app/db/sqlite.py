class Db:
    def __init__(self):
        pass

    def _connect(self):
        import sqlite3
        return sqlite3.connect('dishes', check_same_thread=False)
