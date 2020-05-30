from aiogram import types
from aiogram.dispatcher import FSMContext
from misc import dp, wit
import random
import  orders
from aiogram.dispatcher.filters import Command
import get_pizza_by_contents


@dp.message_handler(Command('start'), state = None)
async def startHandler(message: types.Message):
    print("Получил команду start")
    await message.answer_sticker(sticker = open('static/sticker' + str(random.randint(0, 9)) + '.webp', 'rb'))

    await message.answer(
                     f"Добрый вечер, <b>{message.from_user.first_name}</b>! Захотелось чего-то вкусного?"+ " Я - <b>VivatPizzaBot</b>, буду рад помочь.\r\n\n" +
                     "Сделать заказ очень просто : \r\n" +
                     "  1.  Выберите что-то вкусное из нашего меню vivatpizza.ru напишите список боту\r\n" +
                     "  2.  Напишите мне, на что пал ваш выбор\r\n" +
                     "  3.  Уточните адрес и время доставки"
                     )
    await message.answer("<b>3 самые популярные пиццы за сегодня :</b>\n" + get_pizza_by_contents.get_menu(3))
    await message.answer("Ожидаю список ваш список блюд.")

    #состояние ожидания ввода первого блюда
    await orders.Order.waiting_for_dish.set()


# обработка сообщений , когда мы все еще ожидаем, что пользователь будет вводить блюда
@dp.message_handler(state=orders.Order.waiting_for_dish, content_types=types.ContentTypes.TEXT)
async def food_step_(message: types.Message, state: FSMContext):


    order = orders.get_order(message.from_user.id)

    async with state.proxy() as data:
        data['order_id'] = message.from_user.id

    wit_answer = wit.get_dishes_list(message.text.lower())

    if(wit_answer['intent'][0]['value']) == 'get_menu':
        await message.answer("<b>Меню наших самых любимых пицц:</b>\n" + get_pizza_by_contents.get_menu(10))
        await message.answer("Смогли найти что-то по душе?")
        await orders.Order.waiting_for_dish.set()
        return

    if(wit_answer['constructor']):
        await message.answer("О, вы хотите собрать свою?\n-Без проблем "
                             "\nУ нас есть классный конструктор : https://www.vivatpizza.ru/constructor/konstruktor-piccy")
        return



    dishes = wit_answer['dishes']


    #Проверим салаты
    for dish in dishes:
        if dish['type'] == 'salad':
            order.dishes['salads'].append(orders.Salad(dish))

    #Проверим, что у всех пицц (если они есть) есть размер и вид теста
    #находим все пиццы в заказе
    for dish in dishes:
        if dish['type'] == 'pizza':
            order.dishes['pizzas'].append(orders.Pizza(dish))

    await message.answer("Вы заказали : ")

    dish_name = ""
    for pizza in order.dishes['pizzas']:
        dish_name +=  f"<b>{pizza.name}</b>\n"

    for salad in order.dishes['salads']:
        dish_name +=  f"<b>{salad.name}</b>\n"

    await message.answer(dish_name)

    #Проверяем состояние всех пицц
    need_dough = []
    need_size = []

    for pizza in order.dishes['pizzas']:
        if pizza.dough is None:
            need_dough.append(pizza)
        if pizza.size is None:
            need_size.append(pizza)

    async with state.proxy() as data:
        data["need_dough"] = need_dough
        data["need_size"] = need_size


    data = await state.get_data()
    print(data)
    if len(data['need_dough']) > 0:
        await order.waiting_for_dough.set()
        await message.answer(f"{data['need_dough'][0].name} будет на тонком или на пышном тесте?")
    else:
        if(len(data['need_size']) > 0):
            await orders.get_order(message.from_user.id).waiting_for_size.set()
            await message.answer(f"{data['need_size'][0].name} будет 20см, 31см или 36 см??")
        else:
            await message.answer("Хотели бы вы чего-то еще ?")
            await orders.get_order(message.from_user.id).waiting_for_smth_else.set()


@dp.message_handler(state=orders.Order.waiting_for_dough, content_types=types.ContentTypes.TEXT)
async def dough_step(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print("Все пиццы, которым нужно установить тесто : ")
    pizzas_need_dough = data.get('need_dough')
    for pizza in pizzas_need_dough:
        print(pizza.name)

    current_pizza = data.get('need_dough')[0]

    current_pizza = orders.orders_db[message.from_user.id].get_pizza_by_name(current_pizza.name)
    current_pizza.dough = wit.get_dough(message.text.lower())['size']
    print(current_pizza.get_description())

    async with state.proxy() as data:
        data['need_dough'][0].dough = wit.get_dough(message.text.lower())['size']
        del data['need_dough'][0]

    print("Все пиццы, которым нужно установить тесто : ")
    pizzas_need_dough = data.get('need_dough')
    for pizza in pizzas_need_dough:
        print(pizza.name)

    if len(pizzas_need_dough) > 0:
        await message.answer(f"{pizzas_need_dough[0].name} будет на тонком или на пышном тесте?")
    else:
        data = await state.get_data()
        pizzas_size = data['need_size']
        if(len(pizzas_size) > 0):
            await orders.get_order(message.from_user.id).waiting_for_size.set()
            await message.answer(f"{pizzas_size[0].name} будет 20см, 31см или 36 см??")
        else:
            await message.answer("Хотели бы вы чего-то еще ?")
            await orders.get_order(message.from_user.id).waiting_for_smth_else.set()


@dp.message_handler(state=orders.Order.waiting_for_size, content_types=types.ContentTypes.TEXT)
async def size_step(message: types.Message, state: FSMContext):

    data = await state.get_data()
    pizzas_size_list = data['need_size']
    print("Вызван обработчик размера пиццы", pizzas_size_list[0].name)
    pizzas_size_list[0].size = wit.get_size(message.text.lower())['size']
    current_pizza = orders.orders_db[message.from_user.id].get_pizza_by_name(pizzas_size_list[0].name)
    current_pizza.size = wit.get_size(message.text.lower())['size']


    print(pizzas_size_list[0].get_description())

    async with state.proxy() as data:
        data['need_size'][0].size = wit.get_size(message.text.lower())['size']
        del data['need_size'][0]

    print("Все пиццы, которым нужно установить размер : ")
    pizzas_need_size = data.get('need_size')
    for pizza in pizzas_need_size:
        print(pizza.name)

    if len(pizzas_need_size) > 0:
        await message.answer(f"{pizzas_need_size[0].name} будет 20см, 31см или 36 см?")
    else:
        await message.answer("<b>Ваш заказ : </b>")
        order = orders.orders_db.get(message.from_user.id)

        for pizza in order.dishes['pizzas']:
            await  message.answer(pizza.get_description())

        for salad in order.dishes['salads']:
            await  message.answer(salad.get_description())

        await message.answer(f"Итог:{orders.get_order(message.from_user.id).get_price()}")

        await message.answer("Хотели бы вы чего-то еще ?")
        await orders.get_order(message.from_user.id).waiting_for_smth_else.set()


@dp.message_handler(state=orders.Order.waiting_for_smth_else, content_types=types.ContentTypes.TEXT)
async def size_step(message: types.Message, state: FSMContext):
    print("Обработка : нужно ли чего-то еще")
    if message.text.lower() != 'да':
        await message.answer("Переходим к оформлению заказа. Введите адрес доставки")
        await orders.get_order(message.from_user.id).waiting_for_address.set()
    else:
        await message.answer("Ожидаю список блюд.")
        await orders.get_order(message.from_user.id).waiting_for_dish.set()


@dp.message_handler(state=orders.Order.waiting_for_address, content_types=types.ContentTypes.TEXT)
async def size_step(message: types.Message, state: FSMContext):
    orders.get_order(message.from_user.id).address = message.text
    await message.answer("В какое время вам удобно принять заказ?")
    await orders.get_order(message.from_user.id).waiting_for_time.set()


@dp.message_handler(state=orders.Order.waiting_for_time, content_types=types.ContentTypes.TEXT)
async def size_step(message: types.Message, state: FSMContext):
    orders.get_order(message.from_user.id).time = message.text
    await message.answer("Укажите номер телефона того, кто будет принимать заказ")
    await orders.get_order(message.from_user.id).waiting_for_Ok.set()


@dp.message_handler(state=orders.Order.waiting_for_Ok, content_types=types.ContentTypes.TEXT)
async def size_step(message: types.Message, state: FSMContext):
    orders.get_order(message.from_user.id).phone = message.text
    await message.answer("Спасибо! Мы старались быть полезными(очень-очень ТТ_ТТ)")
    await message.answer(orders.get_order(message.from_user.id).get_description())
