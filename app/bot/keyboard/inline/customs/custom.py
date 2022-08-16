from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.customs.callback_custom import custom_callback


custom_buttons = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(
        text="Аллергии.\nНелюбимые продукты.",
        callback_data=custom_callback.new(custom_button="allergy")
    )]
])
