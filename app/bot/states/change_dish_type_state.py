from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeDishType(StatesGroup):
    dish_id = State()
    dish_type = State()
