import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

CSV = 'breakfast.csv'
HOST = 'https://www.russianfood.com/'
URL = 'https://www.russianfood.com/recipes/bytype/?fid='
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange'
              ';v=b3;q=0.9',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 '
        'Edg/100.0.1185.39'
}
endings = {'926': 1, '927': 2, '928': 3, '4': 4}

def get_html(url, params=''):
    return requests.get(url, headers=HEADERS, params=params)


def get_content(html) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='recipe_l in_seen v2')
    dish = []

    for item in items:
        dish.append({
            'title': item.find(
                'div', class_='title').get_text(strip=True),
            'description': item.find(
                'div', class_='announce').get_text(strip=True),
            'dish_img': HOST + item.find(
                'div', class_='foto').find('img').get('src')
        })
    return dish


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Навание блюда', 'Состав', 'Картинка'])
        for item in items:
            writer.writerow([item['title'],
                             item['description'], item['dish_img']])


def fill_db(items, end):
    df = pd.DataFrame({
        'Навание блюда': ['title'],
        'Состав': ['description'],
        'Картинка': ['dish_img']
    })
    for item in items:
        writer = pd.DataFrame({
            'Навание блюда': [item['title']],
            'Состав': [item['description']],
            'Картинка': (item['dish_img']).replace(
                'www.russianfood.com///', '')
        })
        df = df.append(writer, ignore_index=True)

    # add to db
    from app.db.sqlite import Database

    db = Database()

    for row in df.itertuples():
        result = row.Состав.rsplit('.', 1)[-1]
        result = result.rsplit('!', 1)[-1]
        result = result.split(', ')
        # # add dish to db(dish)
        db.add_dish(row._1, row.Состав, row.Картинка)
        # # add dish type to db(dish_type)
        db.add_dish_type(endings[end], db.get_last_dish_id())
        # # add ingredients to db(ingredient)
        for ingr_name in result:
            db.add_ingredient(ingr_name,)
            # add items to db(dish_ingredient)
            db.add_dish_ingredient(db.get_last_dish_id(), db.get_ingredient_id(ingr_name))


def parser():
    pagenation = input('Количество страниц: ')
    pagenation = int(pagenation.strip())
    for end in endings:
        url_plus_ending = URL + end
        html = get_html(url_plus_ending)
        if html.status_code == 200:
            dish = []
            for page in range(0, pagenation):
                print(f'Парсим страницу {page}')
                html = get_html(url_plus_ending, params={'page': page})
                dish.extend(get_content(html.text))
                # save_doc(dish, CSV)
                fill_db(dish, end)
            pass
        else:
            print('Error')


parser()
