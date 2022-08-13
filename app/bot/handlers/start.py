import sqlite3
from aiogram import types
from aiogram.dispatcher.filters import Command
from app.bot.keyboard.inline import basic_bottons
from app.loader import dp, db


@dp.message_handler(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}.",
                         reply_markup=basic_bottons)
    user_name = message.from_user.full_name
    user_id = message.from_user.id

    try:
        db.add_user(user_id, user_name)
    except sqlite3.IntegrityError as error:
        print(error)
