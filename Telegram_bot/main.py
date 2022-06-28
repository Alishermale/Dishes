import telebot
from telebot import types
from work_with_bd import lunch, breakfast, drink, dinner
import os


#TOKEN = os.environ["TOKEN"]

TOKEN = None

with open('TOKEN.txt') as f:
    TOKEN = f.read().strip()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    buttoms(message)


@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id, 'Я бы тоже отправил стикер, но мой разработчик пока не добавил эту фичу. Ждём что скоро добавит )')


@bot.message_handler(content_types=['voice'])
def get_user_voice(message):
    bot.send_message(message.chat.id, 'Я занят, потом послушаю')


@bot.message_handler(commands=['Вебсайт'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Тут рецепты :)', url='https://www.russianfood.com'))
    bot.send_message(message.chat.id, 'Я беру рецепты пока только с этого сайта: Russianfood', reply_markup=markup)


@bot.message_handler(commands=['Завтрак'])
def send_breakfast(message):
    db_dish = 'Breakfast.csv'
    bot.send_message(message.chat.id, breakfast(db_dish))
    bot.send_message(message.chat.id, breakfast(db_dish))


@bot.message_handler(commands=['Обед'])
def send_lunch(message):
    db_dish = 'Lunch.csv'
    bot.send_message(message.chat.id, lunch(db_dish))
    bot.send_message(message.chat.id, lunch(db_dish))


@bot.message_handler(commands=['Ужин'])
def send_dinner(message):
    db_dish = 'Dinner.csv'
    bot.send_message(message.chat.id, dinner(db_dish))
    bot.send_message(message.chat.id, dinner(db_dish))


@bot.message_handler(commands=['Ужин'])
def send_drink(message):
    db_dish = 'drink.csv'
    bot.send_message(message.chat.id, drink(db_dish))
    bot.send_message(message.chat.id, drink(db_dish))


@bot.message_handler(commands=['Что поесть?'])
def choice(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('Старт')
    breakfast = types.KeyboardButton('Завтрак')
    lunch = types.KeyboardButton('Обед')
    dinner = types.KeyboardButton('Ужин')
    drink = types.KeyboardButton('Напитки')
    markup.add(breakfast, lunch, dinner, drink, start)
    bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)


@bot.message_handler(commands=['help', 'Помощь'])
def buttoms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Вебсайт')
    start = types.KeyboardButton('Старт')
    choice = types.KeyboardButton('Что поесть?')
    markup.add(website, start, choice)
    bot.send_message(message.chat.id, 'Вот кнопки:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Старт"):
        start(message)
    elif(message.text == "Что поесть?"):
        choice(message)
    elif (message.text == "Вебсайт"):
        website(message)
    elif (message.text == "Помощь"):
        buttoms(message)
    elif (message.text == "Завтрак"):
        send_breakfast(message)
    elif (message.text == "Обед"):
        send_lunch(message)
    elif (message.text == "Ужин"):
        send_dinner(message)
    elif (message.text == "Напитки"):
        send_drink(message)


bot.polling(none_stop=True,  timeout=123)
