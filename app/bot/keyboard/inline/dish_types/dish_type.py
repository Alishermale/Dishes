from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.dish_types.callback_dishes_type import dishes_type_callback
from app.loader import db

types = {}
names = db.get_type_names()
buttons = db.get_button_names()
for name, button in zip(names, buttons):
    types[''.join(button)] = ''.join(name)


def type_button(types: dict, rows: int = 2) -> list:
    tb = [
        InlineKeyboardButton(
            text=k,
            callback_data=dishes_type_callback.new(dish_type=types[k])
        )
        for k, v in types.items()
    ]
    return [tb[n:n + rows] for n in range(0, len(tb), rows)]


dishes_type_buttons = InlineKeyboardMarkup(inline_keyboard=type_button(types=types))
