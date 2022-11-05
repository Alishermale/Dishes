from app.db.queries import QUERIES
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "dishes")


class Database:
    def __init__(self, path_to_db=db_path):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        with sqlite3.connect(db_path) as db:
            return db

    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def add_user(self, user_id: int, user_name: str):
        parameters = (user_id, user_name)
        self.execute(sql=QUERIES["add_user"],
                     parameters=parameters, commit=True)

    def deactivate_user(self, user_id):
        self.execute(sql=QUERIES["deactivate_user"], parameters=user_id)

    def update_dish_type(self, dish_id: int, dish_type: str):
        parameters = (dish_type, int(dish_id))
        self.execute(sql=QUERIES["update_dish_type"],
                     parameters=parameters, commit=True)

    def random_dish(self, last_dish_type):
        return self.execute(sql=QUERIES["random_dish"],
                            parameters=(last_dish_type, ), fetchall=True)

    def get_type_names(self):
        return self.execute(sql=QUERIES["get_type_names"], fetchall=True)

    def get_button_names(self):
        return self.execute(sql=QUERIES["get_button_names"], fetchall=True)

    def change_last_dish_type(self, dish_type: str, id: int):
        parameters = (dish_type, id)
        self.execute(sql=QUERIES['change_last_dish_type'], parameters=parameters,
                     commit=True)

    def get_last_dish_type(self, telegram_id: int):
        return ''.join(self.execute(sql=QUERIES['get_last_dish_type'], parameters=(telegram_id, ),
                            fetchall=True)[0])

    def create_user(self):
        self.execute(sql=QUERIES["create_user"], commit=True)

    def create_dish(self):
        self.execute(sql=QUERIES["create_dish"], commit=True)

    def create_ingredient(self):
        self.execute(sql=QUERIES["create_ingredient"], commit=True)

    def create_dish_ingredient(self):
        self.execute(sql=QUERIES["create_dish_ingredient"], commit=True)

    def create_allergy(self):
        self.execute(sql=QUERIES["create_allergy"], commit=True)

    def create_type(self):
        self.execute(sql=QUERIES["create_type"], commit=True)

    def create_dish_type(self):
        self.execute(sql=QUERIES["create_dish_type"], commit=True)
