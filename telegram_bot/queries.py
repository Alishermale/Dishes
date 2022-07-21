# this file for all requests in db
import sqlite3
import pandas as pd


conn = sqlite3.connect('dishes')
c = conn.cursor()

# getting dishes by dishes and join them into db
dish_id = 1
while dish_id < 166:
    dishes = pd.read_csv('drink.csv')
    dish_name = str((dishes.loc[:, "Навание блюда"])[dish_id])
    ingr = (str((dishes.loc[:, "Ингредиенты"])[dish_id]) + '.')
    description = str((dishes.loc[:, "Состав"])[dish_id])
    description = description.replace(ingr, '')
    picture = str((dishes.loc[:, "Картинка"])[dish_id])
    dish_type = '4'

    params = (
        (dish_id + 1808), str(dish_name), str(description), str(ingr.capitalize()), str(picture), str(dish_type)
    )

    c.execute(('''INSERT OR IGNORE INTO dishes VALUES 
                        (?, ?, ?, ?, ?, ?);'''), params)
    dish_id += 1

conn.commit()
c.close()

# c.execute('''INSERT INTO users VALUES (1)''')
