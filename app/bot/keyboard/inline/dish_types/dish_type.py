from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.dish_types.\
    callback_dishes_type import dishes_type_callback
from app.loader import db


def type_button(rows: int = 2) -> list:
    """Takes button names from db, then generate inline buttons"""
    types = {}
    types_name = zip(db.get_type_names(), db.get_button_names())
    for name, button in types_name:
        types[''.join(button)] = ''.join(name)
    generated_buttons = [
        InlineKeyboardButton(
            text=k,
            callback_data=dishes_type_callback.new(dish_type=types[k])
        )
        for k, v in types.items()
    ]
    return [generated_buttons[n:n + rows]
            for n in range(0, len(generated_buttons), rows)]


dishes_type_buttons = InlineKeyboardMarkup(inline_keyboard=type_button())
