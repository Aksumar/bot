from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from misc import dp

class Order(StatesGroup):
    waiting_for_dish = State()
    waiting_for_address = State()
    waiting_for_phone = State()
    waiting_for_time = State()
    
    dishes = []
    address = None
    phone = None
    time = None


class Pizza(StatesGroup):
    waiting_for_size = State()
    waiting_for_dough = State()
