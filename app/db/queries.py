QUERIES = {
    'create_table_dish': '''
              CREATE TABLE IF NOT EXISTS dishes
              ([dish_id] INTEGER PRIMARY KEY AUTOINCREMENT, [dish_name] TEXT,
              [description] TEXT, [ingredient] TEXT, [picture] TEXT,
              [dish_type] TEXT)
              ''',
    'create_table_users': '''
              CREATE TABLE IF NOT EXISTS users
              ([user_id] int NOT NULL,
              [user_name] varchar(255) NOT NULL,
              PRIMARY KEY (user_id))
              ''',
    'add_new_user': 'INSERT INTO users '
                    'VALUES(?, ?)',
    'random_dish': 'SELECT * FROM dishes WHERE dish_type=(?) ORDER BY random() LIMIT 1',
    'delete_user': 'DELETE FROM users WHERE user_id={}',
    'update_dish_type': 'UPDATE dishes SET dish_type = (?) WHERE dish_id = (?)'
}
