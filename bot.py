import time
import telebot
import config
import random
from wit import Wit


from telebot import apihelper

apihelper.proxy = {'https': 'SOCKS5://87.241.90.113:10200'
                   }

bot = telebot.TeleBot(config.token, threaded=False)
token = "VJ56M3RHCYN26M6EPKA3S4XTE5EHMDSU"
client = Wit(token)
resp = client.message("пицца4 сыра")
print(resp)

@bot.message_handler(commands=['start'])
def send_welcome(message):

    sticker = open('static/sticker' + str(random.randint(0, 10)) + '.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("Генерация рандомного числа")
    # item2 = types.KeyboardButton("Как дела?")
    # markup.add(item1, item2)

    question = ["Итак, что же вы выбрали?\nВведите ваш выбор ниже",
                "На что пал ваш выбор сегодня?\nВведите ваш выбор ниже",
                "Чем сегодня будете ужинать?\nВведите ваш выбор ниже"]

    bot.send_message(message.chat.id,
                     "Добрый вечер, <b>{0.first_name}</b>! Захотелось чего-то вкусного?".format(message.from_user) + " Я - <b>VivatPizzaBot</b>, буду рад помочь.\r\n\n" +
                     "Сделать заказ очень просто : \r\n" +
                     "  1.  Выберите что-то вкусное из нашего меню vivatpizza.ru\r\n" +
                     "  2.  Напишите мне, на что пал ваш выбор\r\n" +
                     "  3.  Уточните адрес и время доставки",
                     parse_mode='html')

    bot.send_message(message.chat.id, question[random.randint(0, 2)])

dishes = ["пицца", "бургер", "суп", "закуска", "горячее", "салат"]



@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
    if message.chat.type == 'private':

        print()

        # order = nlp.isOrder(message.text)
        # if(order[0]):
        #     bot.send_message(message.chat.id, "О! Это сообщение с едой")
        #     bot.send_message(message.chat.id, order[1])







while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as ex:
        print(ex.args)
        time.sleep(2)
