from aiogram.types import CallbackQuery
from app.bot.keyboard.inline.callback_custom import custom_callback
from app.loader import dp


@dp.callback_query_handler(custom_callback.filter(custom_button="allergy"))
async def remember_user_allergy(call: CallbackQuery):
    await call.message.answer("Пока не могу запомнить твои"
                              " аллергии. Обратись позже.")
