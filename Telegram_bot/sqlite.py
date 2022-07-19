import sqlite3
import re
import work_with_bd


try:
    conn = sqlite3.connect('dishes')
    c = conn.cursor()
    print("Database created and successfully connected to SQLite")

    # create 2 tables
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

    # geting dishes by dishes and join them into db
    while True:
        dish = work_with_bd.breakfast('Breakfast.csv')
        for s in re.findall(r'\d+', dish[0:5]):
            dish_id = int(s)
        dish_name = dish.replace(str(dish_id), '')
        dish_name = re.findall(r'^\w', dish_name)
        description = re.findall('^\.\n*\.\n\n$', dish)
        ingr = None
        picture = re.findall('^h*jpg$', dish)
        dish_type = '1'

        c.execute(('''INSERT INTO dishes VALUES 
                            (?, ?, ?, ?, ?, ?);'''), (dish_id, str(dish_name), str(description), str(ingr), str(picture), str(dish_type)))
        break

    #c.execute('''INSERT INTO users VALUES (1)''')

    conn.commit()
    c.close()

except sqlite3.Error as error:
    print("Error connecting to sqlite", error)
finally:
    if (conn):
        conn.close()
        print("SQLite connection closed")
