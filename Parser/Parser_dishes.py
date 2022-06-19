import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


CSV = 'drink.csv'
HOST = 'https://www.russianfood.com/'
URL = 'https://www.russianfood.com/recipes/bytype/?fid=4'#Возникает ошибка AttributeError: 'NoneType' object has no attribute 'get_text', если поменять последние цифры, то ошибка проходит
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'
}


def get_html(url, params=''):
    return  requests.get(url, headers=HEADERS, params=params)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='recipe_l in_seen v2')
    drink = []

    for item in items:
        drink.append({
            'title': item.find('div', class_='title').get_text(strip=True),
            'description': item.find('div', class_='announce').get_text(strip=True),
            'ingrediets': item.find('div', class_='ingr_str').get_text(strip=True),
            'dish_img': HOST + item.find('div', class_='foto').find('img').get('src')
        })
    return drink


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Навание блюда', 'Состав', 'Ингредиенты', 'Картинка'])
        for item in items:
            writer.writerow([item['title'], item['description'], item['ingrediets'], item['dish_img']])


def save_doc2(items):
    with open('drink.csv', 'w', newline='', encoding='UTF-8') as file:
        df = pd.DataFrame({
            'Навание блюда': ['title'],
            'Состав': ['description'],
            'Ингредиенты': ['ingrediets'],
            'Картинка': ['dish_img']
        })
        for item in items:
            writer = pd.DataFrame({
                'Навание блюда': [item['title']],
                'Состав': [item['description']],
                'Ингредиенты': item['ingrediets'],
                'Картинка': (item['dish_img']).replace('www.russianfood.com///', '')
            })
            df = df.append(writer, ignore_index=True)
            df.to_csv('drink.csv')


def parser():
    pagenation = input('Количество страниц: ')
    pagenation = int(pagenation.strip())
    html = get_html(URL)
    if html.status_code == 200:
        drink = []
        for page in range(0, pagenation):
            print(f'Парсим страницу {page}')
            html = get_html(URL, params={'page': page})
            drink.extend(get_content(html.text))
            #save_doc(drink, CSV)
            save_doc2(drink)
        pass
    else:
        print('Error')


parser()
