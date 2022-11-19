from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.under_dishes.callback_under_dish import under_dish_callback


under_dish_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Другой тип.",
            callback_data=under_dish_callback.new(step='another_type')
        ),
        InlineKeyboardButton(
            text="Следующий.",
            callback_data=under_dish_callback.new(step='next')
        )
    ]
])
