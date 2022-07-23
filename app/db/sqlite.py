# this will be a db functions.
# not completed.
import sqlite3


try:
    conn = sqlite3.connect('dishes')
    c = conn.cursor()
    print("Database created and successfully connected to SQLite")

    # create 2 tables
    c.execute('''
              CREATE TABLE IF NOT EXISTS dishes
              ([dish_id] INTEGER PRIMARY KEY AUTOINCREMENT, [dish_name] TEXT,
              [description] TEXT, [ingredient] TEXT, [picture] TEXT,
              [dish_type] TEXT)
              ''')

    c.execute('''
              CREATE TABLE IF NOT EXISTS users
              ([user_id] INTEGER PRIMARY KEY AUTOINCREMENT)
              ''')

    conn.commit()
    c.close()

except sqlite3.Error as error:
    print("Error connecting to sqlite", error)
finally:
    if conn:
        conn.close()
        print("SQLite connection closed")
