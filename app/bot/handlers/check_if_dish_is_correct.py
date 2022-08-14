import os
import sqlite3

from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from app.bot.states import ChangeDishType
from app.db.queries import QUERIES
from app.loader import dp

conn = sqlite3.connect('/home/alishermale/Python/My_projects/dishes/app/db/dishes', check_same_thread=False)
c = conn.cursor()
load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
admin_id = os.getenv('ADMIN_ID')


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


@dp.message_handler(state=ChangeDishType.dish_type)
async def correct_dish_type(message: types.Message, state: FSMContext):
    data = await state.get_data()
    dish_id = data.get("answer1")
    dish_type = message.text
    await state.update_data(answer2=dish_type)
    await message.answer(f"Отлично, данные принял.\n{dish_id}, {dish_type}")
    try:
        c.execute(QUERIES.get('update_dish_type').format(dish_type, dish_id))
        conn.commit()
    except Exception as err:
        await message.answer(F"Ошибка {err}")
    await state.finish()
