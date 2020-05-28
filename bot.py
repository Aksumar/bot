from aiogram import Bot, Dispatcher, executor
from config import token_tg
import handlers


bot = Bot(token_tg, parse_mode="HTML", proxy='http://104.255.174.119:15599')
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp, send_to_admin

    executor.start_polling(dp, on_startup=send_to_admin)
