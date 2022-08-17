# get dish card.
import os
import sqlite3
from aiogram.types import CallbackQuery
from dotenv import load_dotenv
from app.bot.keyboard.inline import under_dish_buttons
from app.bot.keyboard.inline import dishes_type_callback
from app.bot.keyboard.inline import under_dish_callback
from app.db.queries import QUERIES
from app.loader import dp

conn = sqlite3.connect('/home/alishermale/Python/My_projects/dishes/'
                       'app/db/dishes', check_same_thread=False)
c = conn.cursor()
last_dish_type = ""
load_dotenv()
admins = os.getenv("ADMIN_ID")


@dp.callback_query_handler(under_dish_callback.filter(step="next"))
async def next_button(call: CallbackQuery, dish_type: str = None):
    global last_dish_type
    if dish_type:
        last_dish_type = dish_type
        # for admins dish card will be with dish_id and dish_type.
        # that will be helpful to see if dish_type incorrect.
    if call.from_user.id == int(admins):
        d_mess = c.execute(QUERIES.get('random_dish'),
                           last_dish_type).fetchone()
        photo = d_mess[-2]
        caption = (d_mess[:-2], d_mess[-1])
    else:
        d_mess = c.execute(QUERIES.get('random_dish'),
                           last_dish_type).fetchone()[1:-1]
        photo = d_mess[-1]
        caption = (d_mess[:-1])
    await call.message.answer_photo(photo, caption=caption,
                                    reply_markup=under_dish_buttons)


@dp.callback_query_handler(dishes_type_callback.filter(
    dish_type=("breakfast", "lunch", "dinner", "drink")))
async def send_drink(call: CallbackQuery):
    dish_types = {
        "breakfast": "1",
        "lunch": "2",
        "dinner": "3",
        "drink": "4"
    }
    await next_button(call, dish_type=dish_types[call.data.split(":")[-1]])
