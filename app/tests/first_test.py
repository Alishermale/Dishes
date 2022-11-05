from app.db.sqlite import Database


# inicializacion db
__init_db__ = Database()


# create tables
def test_create_type():
    __init_db__.create_type()


def test_create_ingredient():
    __init_db__.create_ingredient()


def test_create_user():
    __init_db__.create_user()


def test_create_dish():
    __init_db__.create_dish()


def test_create_dish_ingredient():
    __init_db__.create_dish_ingredient()


def test_create_allergy():
    __init_db__.create_allergy()


def test_create_dish_type():
    __init_db__.create_dish_type()


# fill db
def test_fill_type():
    __init_db__.execute(sql='''INSERT INTO type(type_name, button_name)
    VALUES ('breakfast', 'Завтрак'), ('lunch', 'Обед'), ('dinner', 'Ужин'),
     ('drink', 'Напитки'), ('salat', 'Салат')''', commit=True)


def test_fill_ingredient():
    __init_db__.execute(sql='''INSERT INTO ingredient(ingredient_name)
    VALUES ('tea'), ('sugar'), ('tea'), ('sugar')''', commit=True)


def test_fill_user():
    __init_db__.execute(sql='''INSERT INTO user(full_name, telegram_id, last_dish_type)
    VALUES ('Maxim', 1234, 'breakfast'), ('Pedro', 4321, 'lunch'), ('Hurry', 8490, 'drink')''', commit=True)


def test_fill_dish():
    __init_db__.execute(sql='''INSERT INTO dish(title, description, picture, user_id)
    VALUES  ('tea', 'sweet tea', 'dkfjaljka', 1), ('sweet sugar', 'just a sweet sugar', 'asdfjkl;', 1)''', commit=True)


def test_test_dish_ingredient():
    __init_db__.execute(sql='''INSERT INTO dish_ingredient(dish_id, ingredient_id)
    VALUES  (2, 1), (2, 1), (1, 2)''', commit=True)


def test_test_allergy():
    __init_db__.execute(sql='''INSERT INTO allergy(allergy_name, ingredient_id, user_id)
    VALUES  ('celery', 1, 1), ('peanuts', 1, 2), ('dioxide', 2, 1)''', commit=True)


def test_test_dish_type():
    __init_db__.execute(sql='''INSERT INTO dish_type(type_id, dish_id)
    VALUES  (1, 1), (1, 2), (2, 1)''', commit=True)


# delete db
# def test_delete_db():
#     __init_db__.execute(sql='''drop table dish''')
#     __init_db__.execute(sql='''drop table user''')
#     __init_db__.execute(sql='''drop table ingredient''')
#     __init_db__.execute(sql='''drop table type''')
#     __init_db__.execute(sql='''drop table dish_type''')
#     __init_db__.execute(sql='''drop table dish_ingredient''')
#     __init_db__.execute(sql='''drop table allergy''')
