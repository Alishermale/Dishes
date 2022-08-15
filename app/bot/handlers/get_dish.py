import os
import sqlite3
from aiogram.types import CallbackQuery
from dotenv import load_dotenv
from app.bot.keyboard.inline import under_dish_buttons
from app.bot.keyboard.inline.callback_dishes_type import dishes_type_callback
from app.bot.keyboard.inline.callback_under_dish import under_dish_callback
from app.db.queries import QUERIES
from app.loader import dp

conn = sqlite3.connect('/home/alishermale/Python/My_projects/dishes/'
                       'app/db/dishes', check_same_thread=False)
c = conn.cursor()
last_dish_type = ""
load_dotenv()
admins = os.getenv("ADMIN_ID")


@dp.callback_query_handler(under_dish_callback.filter(step="next"))
async def next_button(call: CallbackQuery):
    if call.from_user.id == int(admins):
        d_mess = c.execute(QUERIES.get('random_dish'), last_dish_type).fetchone()
        photo = d_mess[-2]
        caption = (d_mess[:-2], d_mess[-1])
    else:
        d_mess = c.execute(QUERIES.get('random_dish'), last_dish_type).fetchone()[1:-1]
        photo = d_mess[-1]
        caption = (d_mess[:-1])
    await call.message.answer_photo(photo, caption=caption,
                                    reply_markup=under_dish_buttons)


async def sql_requests(call: CallbackQuery, dish_type: str):
    global last_dish_type
    if call.from_user.id == int(admins):
        d_mess = c.execute(QUERIES.get('random_dish'), dish_type).fetchone()
        photo = d_mess[-2]
        caption = (d_mess[:-2], d_mess[-1])
    else:
        d_mess = c.execute(QUERIES.get('random_dish'), dish_type).fetchone()[1:-1]
        photo = d_mess[-1]
        caption = (d_mess[:-1])
    last_dish_type = dish_type
    await call.message.answer_photo(photo, caption=caption,
                                    reply_markup=under_dish_buttons)


@dp.callback_query_handler(dishes_type_callback.filter(dish_type="breakfast"))
async def send_breakfast(call: CallbackQuery):
    await sql_requests(call, dish_type='1')


@dp.callback_query_handler(dishes_type_callback.filter(dish_type="lunch"))
async def send_lunch(call: CallbackQuery):
    await sql_requests(call, dish_type='2')


@dp.callback_query_handler(dishes_type_callback.filter(dish_type="dinner"))
async def send_dinner(call: CallbackQuery):
    await sql_requests(call, dish_type='3')


@dp.callback_query_handler(dishes_type_callback.filter(dish_type="drink"))
async def send_drink(call: CallbackQuery):
    await sql_requests(call, dish_type='4')
