import sqlite3
import re
import work_with_bd


try:
    conn = sqlite3.connect('dishes')
    c = conn.cursor()
    print("База данных создана и успешно подключена к SQLite")

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
    c.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
