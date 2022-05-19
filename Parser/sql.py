import os
import csv
from random import randint

my_path = r'C:\Python\Projects\Pet_project_dishes\Parser\Data'
index = 10
value = '7585'


def dinner():
    for file in os.listdir(my_path):
        path_file = os.path.join(my_path, 'dishes.csv')
        with open(path_file, 'r') as output:
            reader = csv.reader(output, delimiter=";")
            read = [row for row in reader if row]
            for row in read:
                return read[randint(1, 184)]


def breakfast():
    for file in os.listdir(my_path):
        path_file = os.path.join(my_path, 'breakfast.csv')
        with open(path_file, 'r') as output:
            reader = csv.reader(output, delimiter=";")
            read = [row for row in reader if row]
            for row in read:
                return read[randint(1, 103)]


def lunch():
    for file in os.listdir(my_path):
        path_file = os.path.join(my_path, 'lunch.csv')
        with open(path_file, 'r') as output:
            reader = csv.reader(output, delimiter=";")
            read = [row for row in reader if row]
            for row in read:
                return read[randint(1, 125)]


