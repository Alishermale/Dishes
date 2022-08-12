from aiogram import types
from aiogram.dispatcher.filters import Command

from app.bot.keyboard.inline import basic_bottons
from app.loader import dp


@dp.message_handler(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}.",
                         reply_markup=basic_bottons)