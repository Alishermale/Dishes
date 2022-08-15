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

    def create_table_users(self):
        sql = QUERIES["create_table_users"]
        self.execute(sql, commit=True)

    def add_user(self, user_id: int, user_name: str):
        parameters = (user_id, user_name)
        self.execute(sql=QUERIES["add_new_user"],
                     parameters=parameters, commit=True)

    def delete_user(self, user_id):
        self.execute(sql=QUERIES["delete_user"], parameters=user_id)

    def update_dish_type(self, dish_id: int, dish_type: str):
        parameters = (dish_type, int(dish_id))
        self.execute(sql=QUERIES["update_dish_type"],
                     parameters=parameters, commit=True)
