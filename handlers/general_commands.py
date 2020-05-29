from aiogram import types
from aiogram.dispatcher import FSMContext
from misc import dp, wit
import random
import  orders


@dp.message_handler(commands=['start'])
async def startHandler(message: types.Message):
    print("Получил команду start")
    await message.answer_sticker(sticker = open('static/sticker' + str(random.randint(0, 9)) + '.webp', 'rb'))

    await message.answer(
                     f"Добрый вечер, <b>{message.from_user.first_name}</b>! Захотелось чего-то вкусного?"+ " Я - <b>VivatPizzaBot</b>, буду рад помочь.\r\n\n" +
                     "Сделать заказ очень просто : \r\n" +
                     "  1.  Выберите что-то вкусное из нашего меню vivatpizza.ru\r\n" +
                     "  2.  Напишите мне, на что пал ваш выбор\r\n" +
                     "  3.  Уточните адрес и время доставки"
                     )

    await message.answer("Ожидаю список блюд")

    #состояние ожидания ввода первого блюда
    await orders.Order.waiting_for_dish.set()


# обработка сообщений , когда мы все еще ожидаем, что пользователь будет вводить блюда
@dp.message_handler(state=orders.Order.waiting_for_dish, content_types=types.ContentTypes.TEXT)
async def food_step_(message: types.Message, state: FSMContext):
    wit_answer = wit.get_dishes_list('Охотничья с каперсами, пеперони и 4 сыра')
    print(wit_answer)
    print("\n")
    dishes = wit_answer['dishes']
    print(dishes)

    #Проверим, что у всех пицц (если они есть) есть размер и вид теста

    pizzas = []
    for dish in dishes:
        if dish['type'] == 'pizza':
            pizzas.append(dish)

    print(pizzas)

    await message.answer("Это обработчик, который включается, когда бот считает, что в сообщении выше какая-то еда")
