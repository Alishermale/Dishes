QUERIES = {
    'add_user': '''INSERT INTO user(telegram_id, full_name) VALUES(?, ?)''',
    'random_dish': '''SELECT d.*, i.ingredient_name FROM dish d INNER JOIN dish_type dt
                        ON d.id = dt.dish_id INNER JOIN type t
                        ON dt.type_id = t.id INNER JOIN dish_ingredient di
                        ON d.id = di.dish_id INNER JOIN ingredient i
                        ON di.ingredient_id = i.id WHERE type_name = (?)
                        ORDER BY random() LIMIT 1''',
    'deactivate_user': 'DELETE FROM user WHERE user_id=(?)',
    'update_dish_type': 'UPDATE dish SET dish_type=(?) WHERE dish_id=(?)',
    'get_type_names': 'SELECT type_name FROM type',
    'get_button_names': 'SELECT button_name FROM type',
    'change_last_dish_type': 'UPDATE user SET last_dish_type=(?) WHERE telegram_id=(?)',
    'get_last_dish_type': 'SELECT last_dish_type FROM user WHERE telegram_id=(?)',
    'create_user': '''CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(128) NOT NULL,
    is_active BIT(1) DEFAULT 1 NOT NULL,
    telegram_id VARCHAR(15) NOT NULL,
    last_dish_type VARCHAR(50)  DEFAULT 'drink'
);''',
    'create_dish': '''CREATE TABLE dish(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(150) NOT NULL,
    description VARCHAR(800) NOT NULL,
    picture CHAR(67) NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);''',
    'create_ingredient': '''CREATE TABLE ingredient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name VARCHAR(100) NOT NULL
);''',
    'create_dish_ingredient': '''CREATE TABLE dish_ingredient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    FOREIGN KEY (dish_id) REFERENCES dish(id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredient(id)
);''',
    'create_allergy': '''CREATE TABLE allergy(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    allergy_name VARCHAR(100) DEFAULT NULL,
    ingredient_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (ingredient_id) REFERENCES ingredient(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
)''',
    'create_type': '''CREATE TABLE type(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name VARCHAR(80) NOT NULL,
    button_name VARCHAR(80)
);''',
    'create_dish_type': '''CREATE TABLE dish_type(
    id INTEGER
     PRIMARY KEY AUTOINCREMENT,
     type_id INTEGER NOT NULL,
     dish_id INTEGER NOT NULL,
    FOREIGN KEY (type_id) REFERENCES type(id),
    FOREIGN KEY (dish_id) REFERENCES dish(id)
);''',
    'update_allergy': '''UPDATE allergy
SET allergy_name = (SELECT ingredient_name 
                    FROM ingredient INNER JOIN allergy 
                    ON ingredient.id = ingredient_id
                    WHERE ingredient.id = ingredient_id)
WHERE allergy_name IS NULL;'''
}
