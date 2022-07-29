QUERIES = {
    'create_table_dish': '''
              CREATE TABLE IF NOT EXISTS dishes
              ([dish_id] INTEGER PRIMARY KEY AUTOINCREMENT, [dish_name] TEXT,
              [description] TEXT, [ingredient] TEXT, [picture] TEXT,
              [dish_type] TEXT)
              ''',
    'create_table_users': '''
              CREATE TABLE IF NOT EXISTS users
              ([user_id] INTEGER PRIMARY KEY AUTOINCREMENT,
              [user_name] TEXT)
              ''',
    'insert': 'INSERT OR IGNORE INTO',
    'random_dish': 'SELECT {} FROM dishes '
                   'WHERE dish_type={} ORDER BY random() LIMIT 1'
}
