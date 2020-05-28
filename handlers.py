from bot import bot, dp
from aiogram.types import Message


async def send_to_admin(*args):
    print("smth")


@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, ты написал: {message.text}"
    await message.reply(text=text)
