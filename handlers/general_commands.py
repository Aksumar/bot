from bot import dp
from aiogram import types

@dp.message_handler(commands=['start'])
async def startHandler(message: types.Message):

