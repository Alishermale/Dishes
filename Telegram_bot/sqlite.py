import sqlite3


conn = sqlite3.connect('dishes')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS dishes
          ([dish_id] INTEGER PRIMARY KEY, [dish_name] TEXT,
          [description] TEXT, [ingredient] TEXT, [picture] TEXT,
          [dish_type] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([user_id] INTEGER PRIMARY KEY)
          ''')


conn.commit()
