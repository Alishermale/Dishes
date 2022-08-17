# possibility for admins to change dish type if that's wrong.
import os
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from app.bot.states import ChangeDishType
from app.db import sqlite
from app.loader import dp, db


conn = sqlite.Database.connection
load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
admin_id = os.getenv('ADMIN_ID')


# start collection of information.
# get dish_id of incorrect dish and new correct dish type.
@dp.message_handler(Text(equals="Ошибка"), user_id=admin_id)
async def command_start(message: types.Message):
    await message.answer("Какой id у блюда?")
    await ChangeDishType.first()


@dp.message_handler(state=ChangeDishType.dish_id)
async def get_dish_id(message: types.Message, state: FSMContext):
    dish_id = message.text
    await message.answer("Спасибо. Теперь введи нужный тип блюда")
    await state.update_data(answer1=dish_id)
    await ChangeDishType.next()


# finish collection of information.
# change dish_type.
@dp.message_handler(state=ChangeDishType.dish_type)
async def correct_dish_type(message: types.Message, state: FSMContext):
    data = await state.get_data()
    dish_id = data.get("answer1")
    dish_type = message.text
    await state.update_data(answer2=dish_type)
    await message.answer(f"Отлично, данные принял.\n{dish_id}, {dish_type}")
    try:
        db.update_dish_type(dish_id, dish_type)
    except Exception as err:
        print(err)
        await message.answer("Произошла ошибка при изменении типа блюда,"
                             "пожалуйста проверьте правильность вводимых"
                             " данных и повторите попытку.")
    await state.finish()
