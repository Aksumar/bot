from aiogram import executor
from misc import dp
import handlers



def on_start():
    print("Vivat бот запущен")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start())
