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
    'update_dish_type': 'UPDATE dishes SET dish_type = (?) WHERE dish_id = (?)',
    'create_db': '''CREATE TABLE user(
    id INT PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128),
    telegram_id CHAR(10),
    last_dish_type VARCHAR(50)
);
CREATE TABLE dish(
    id INT PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(150),
    description VARCHAR(800),
    picture CHAR(67),
    user_id INT FOREIGN KEY REFERENCES user(id)
);
CREATE TABLE ingredient(
    id INT PRIMARY KEY AUTOINCREMENT,
    ingredient_name VARCHAR(100)
);
CREATE TABLE dish_ingredient(
    id INT PRIMARY KEY AUTOINCREMENT,
    dish_id FOREIGN KEY REFERENCES dish(id),
    ingredient_id FOREIGN KEY REFERENCES ingredient(id)
);
CREATE TABLE allergy(
    id INT PRIMARY KEY AUTOINCREMENT,
    allergy_name VARCHAR(100),
    ingredient_id INT FOREIGN KEY REFERENCES ingredient(id),
    user_id INT FOREIGN KEY REFERENCES user(id)
);
CREATE TABLE type(
    id INT PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(80)
);
CREATE TABLE dish_type(
    id INT PRIMARY KEY AUTOINCREMENT,
    type_id INT FOREIGN KEY REFERENCES type(id),
    dish_id INT FOREIGN KEY REFERENCES dish(id)
);'''
}
