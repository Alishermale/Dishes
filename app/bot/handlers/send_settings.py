# customization user's profile.
from aiogram.types import CallbackQuery
from app.bot.keyboard.inline import custom_buttons
from app.bot.keyboard.inline import basic_callback
from app.loader import dp


# send buttons for custom to user
@dp.callback_query_handler(basic_callback.filter(button_name="settings"))
async def send_settings_to_user(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Тут ты можешь настроить бота под себя."
                              "\nПопробуй.",
                              reply_markup=custom_buttons)
