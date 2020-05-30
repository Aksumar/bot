from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from misc import dp
import prices


class Order(StatesGroup):
    waiting_for_dish = State()
    waiting_for_dough = State()
    waiting_for_size = State()
    waiting_for_smth_else = State()
    waiting_for_address = State()
    waiting_for_phone = State()
    waiting_for_time = State()
    waiting_for_Ok = State()
    
    dishes = {'pizzas': [], 'salads': []}

    address = None
    phone = None
    time = None

    def get_pizza_by_name(self,name):
        for pizza in self.dishes['pizzas']:
            if pizza.name == name:
                return pizza

    def get_price(self):
        price = 0
        for pizza in self.dishes['pizzas']:
            if(pizza.price is not None):
                price += pizza.price
            else:
                price += 325
        for salad in self.dishes['salads']:
            if salad.price is not None:
                price += salad.price
            else:
                price += 220
        return price

    def get_description(self):
        result = ''
        for pizza in self.dishes['pizzas']:
            result += f"{pizza.get_description()}\n"
        for salad in self.dishes['salads']:
            result += f"{salad.get_description()}\n"
        result += f"Адрес : {self.address}"
        result += f"Телефон : {self.phone}"
        result += f"Время доставки : {self.time}"

        return result



class Pizza(StatesGroup):
    name = None
    dough = None
    size = None
    price = None
    addons = None

    def __init__(self, pizza_raw):
        self.name = pizza_raw['value']
        self.dough = pizza_raw['dough']
        self.size = pizza_raw['size']
        self.addons = pizza_raw['addons']

    def get_description(self):
        result = f"{self.name} диаметром {self.size}см, тесто {self.dough}"
        if self.addons is not None:
            result += f" со следующими добавками : {self.addons}"
        if self.size is not None:
            self.price = prices.get_pizza_price(self.name, self.dough,int(self.size))
            result += f" ->  {self.price}"
        return result



class Salad:
    name = None
    price = None
    addons = None

    def __init__(self, salad_raw):
        self.name = salad_raw['value']
        self.addons = salad_raw['addons']

    def get_description(self):
        return f"{self.name} {self.addons}"


orders_db = {}

def get_order(id):
    if id not in orders_db:
        orders_db[id] = Order()
    return orders_db[id]

