async def on_startup(dp):
    from app.bot.utils.startup_notify_admins import on_startup_notify
    await on_startup_notify(dp)


if __name__ == '__main__':
    from aiogram import executor
    from bot.handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
