# get dish card.
from aiogram.types import CallbackQuery
from dotenv import load_dotenv
from app.bot.data.config import admin_id
from app.bot.keyboard.inline import under_dish_buttons
from app.bot.keyboard.inline import dishes_type_callback
from app.bot.keyboard.inline import under_dish_callback
from app.db import sqlite
from app.loader import dp, db

conn = sqlite.Database.connection
last_dish_type = ""
load_dotenv()


# send dish and buttons to user
@dp.callback_query_handler(under_dish_callback.filter(step="next"))
async def next_button(call: CallbackQuery, dish_type: str = None):
    global last_dish_type
    if dish_type:
        last_dish_type = dish_type
    # for admins dish card will be with dish_id and dish_type.
    # that will be helpful to see if dish_type incorrect.
    if call.from_user.id == int(admin_id):
        d_mess = db.random_dish(last_dish_type)
        photo = d_mess[0][-2]
        caption = (d_mess[0][:-2], d_mess[0][-1])
    else:
        d_mess = db.random_dish(last_dish_type)
        photo = d_mess[0][-2]
        caption = (d_mess[0][:-1])
    await call.message.answer_photo(photo, caption=caption,
                                    reply_markup=under_dish_buttons)


@dp.callback_query_handler(dishes_type_callback.filter(
    dish_type=("breakfast", "lunch", "dinner", "drink")))
async def send_drink(call: CallbackQuery):
    dish_types = {
        "breakfast": "breakfast",
        "lunch": "lunch",
        "dinner": "dinner",
        "drink": "drink"
    }
    await next_button(call, dish_type=dish_types[call.data.split(":")[-1]])
