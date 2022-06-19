import pandas as pd
import os
import csv
import random
import re


my_path = r'/home/alishermale/Python/My_projects/Startup_dishes/Telegram_bot'

capital_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
spare_symbols = "[]\"'"


def dec_for_dishes(func):
    def inner(*args, **kwargs):
        path_file = os.path.join(my_path, *args, **kwargs)
        with open(path_file, 'r') as output:
            reader = csv.reader(output, delimiter='q')
            read = [row for row in reader if row]
            rand_num = random.randint(1, len(read) - 1)
            rand_row = str(read[rand_num]).replace('h', '\n' + 'h')
            rand_row = rand_row.replace(',', '.', 2)
            Dish = pd.read_csv(*args, **kwargs)
            for s in re.findall(r'\d+', rand_row[0:5]):
                num = int(s)
            ingr = str((Dish.loc[:, "Ингредиенты"])[num])
            for letter in capital_letters:
                rand_row = rand_row.replace(letter, '\n' + letter)
            for symbol in spare_symbols:
                rand_row = rand_row.replace(symbol, '')
            return rand_row.replace(ingr, '').replace('h', '\n' + 'Состав:' + '\n' + ingr.capitalize() + '.' + '\n' + 'h')
    return inner


@dec_for_dishes
def lunch(*args, **kwargs):
    return lunch


@dec_for_dishes
def dinner(*args, **kwargs):
    return dinner


@dec_for_dishes
def breakfast(*args, **kwargs):
    return breakfast


@dec_for_dishes
def drink(*args, **kwargs):
    return drink

