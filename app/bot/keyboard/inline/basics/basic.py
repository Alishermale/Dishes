from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.basics.callback_basic import basic_callback


basic_bottons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Что поесть?",
            callback_data=basic_callback.new(button_name='get_dish')
        )
    ],
    [
        InlineKeyboardButton(
            text="Настройки.",
            callback_data=basic_callback.new(button_name='settings')
        )
    ]
])
