import telebot
from telebot import types
from Parser.sql import dinner, breakfast, lunch

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
    bot.send_message(message.chat.id, breakfast())
    bot.send_message(message.chat.id, breakfast())


@bot.message_handler(commands=['Обед'])
def send_lunch(message):
    bot.send_message(message.chat.id, lunch())
    bot.send_message(message.chat.id, lunch())


@bot.message_handler(commands=['Ужин'])
def send_dinner(message):
    bot.send_message(message.chat.id, dinner())
    bot.send_message(message.chat.id, dinner())


@bot.message_handler(commands=['Что поесть?'])
def choice(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('Старт')
    breakfast = types.KeyboardButton('Завтрак')
    lunch = types.KeyboardButton('Обед')
    dinner = types.KeyboardButton('Ужин')
    markup.add(breakfast, lunch, dinner, start)
    bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)


@bot.message_handler(commands=['help', 'Помощь'])
def buttoms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
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


bot.polling(none_stop=True)
