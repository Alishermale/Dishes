# get dish card.
from aiogram.types import CallbackQuery
from dotenv import load_dotenv
from app.bot.data.config import admin_id
from app.bot.keyboard.inline import under_dish_buttons
from app.bot.keyboard.inline import dishes_type_callback
from app.bot.keyboard.inline import under_dish_callback
from app.loader import dp, db


load_dotenv()
types = db.get_all_types()
all_types = ()
for d_type in types:
    all_types += d_type


# send dish and buttons to user
@dp.callback_query_handler(under_dish_callback.filter(step="next"))
async def next_button(call: CallbackQuery, dish_type: str = None):
    last_dish_type = db.get_last_dish_type(call.from_user.id)
    if dish_type:
        db.change_last_dish_type(dish_type, call.from_user.id)
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
    dish_type=all_types))
async def send_drink(call: CallbackQuery):
    await next_button(call, dish_type=call.data.split(":")[-1])
