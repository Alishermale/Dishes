from aiogram.types import CallbackQuery
from app.bot.keyboard.inline import dishes_type_buttons
from app.bot.keyboard.inline.callback_basic import basic_callback
from app.bot.keyboard.inline.callback_under_dish import under_dish_callback
from app.loader import dp


@dp.callback_query_handler(under_dish_callback.filter(step="another_type"))
@dp.callback_query_handler(basic_callback.filter(button_name='get_dish'))
async def what_to_eat(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Ты можешь выбрать что-то из этого.",
                              reply_markup=dishes_type_buttons)
