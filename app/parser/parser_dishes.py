import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


CSV = 'breakfast.csv'
HOST = 'https://www.russianfood.com/'
URL = 'https://www.russianfood.com/recipes/bytype/?fid=926,927'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange'
              ';v=b3;q=0.9',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 '
        'Edg/100.0.1185.39'
}


def get_html(url, params=''):
    return requests.get(url, headers=HEADERS, params=params)


def get_content(html) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='recipe_l in_seen v2')
    breakfast = []

    for item in items:
        breakfast.append({
            'title': item.find(
                'div', class_='title').get_text(strip=True),
            'description': item.find(
                'div', class_='announce').get_text(strip=True),
            'dish_img': HOST + item.find(
                'div', class_='foto').find('img').get('src')
        })
    return breakfast


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Навание блюда', 'Состав', 'Картинка'])
        for item in items:
            writer.writerow([item['title'],
                             item['description'], item['dish_img']])


def save_doc2(items):
    with open('file.csv', 'w', newline='', encoding='UTF-8'):
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
            df.to_csv('file.csv')


def parser():
    pagenation = input('Количество страниц: ')
    pagenation = int(pagenation.strip())
    html = get_html(URL)
    if html.status_code == 200:
        breakfast = []
        for page in range(0, pagenation):
            print(f'Парсим страницу {page}')
            html = get_html(URL, params={'page': page})
            breakfast.extend(get_content(html.text))
            save_doc(breakfast, CSV)
            save_doc2(breakfast)
        pass
    else:
        print('Error')


parser()
