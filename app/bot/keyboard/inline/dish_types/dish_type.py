from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.dish_types.callback_dishes_type import dishes_type_callback


dishes_type_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Завтрак",
            callback_data=dishes_type_callback.new(dish_type="breakfast")
        ),
        InlineKeyboardButton(
            text="Обед",
            callback_data=dishes_type_callback.new(dish_type="lunch")
        )
    ],
    [
        InlineKeyboardButton(
            text="Ужин",
            callback_data=dishes_type_callback.new(dish_type="dinner")
        ),
        InlineKeyboardButton(
            text="Напитки",
            callback_data=dishes_type_callback.new(dish_type="drink")
        )
    ]
])
