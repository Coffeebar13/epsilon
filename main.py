import random, config

from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import requests as r
from yandex_music import Client
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(config.token)
dp = Dispatcher(bot)

emojies =['⭐', '❤️', '🔥', '✨', '👨‍💻', '👨‍🔧']
errors = ['Я не понял! Напиши что-то менее остроумное.', "Моя твоя не понимать! Пиши понятнее.", "Ошибка: БотСлишкомТупойЧтобыЭтоПонять!", "Ничего не понимаю!", "Сорри, май брейн ис туу смол ту андерстенд тхис!"]
last_jokes = []

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    global emojies
    #await bot.send_message(message.from_user.id, text=message.from_user.id)
    name = message.from_user.first_name
    if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
        await bot.send_message(message.from_user.id, text=f"Здравствуйте, {name}!")
    else:
        await bot.send_message(message.from_user.id, text=f"Здравствуйте, {name}! " + random.choice(emojies))

@dp.message_handler()
async def jokes(message: types.Message):
    global errors
    if message.text == "Анекдот":
        url = 'https://www.anekdot.ru/release/anekdot/day/'
        html = r.get(url)
        soup = bs(html.text, 'html.parser')
        print(random.choice(soup.select(".text")).text)
    else:
        await bot.send_message(message.from_user.id, text=random.choice(errors))

# greeting = ["Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи"]
# hellower = ["Аве", "Салам", "Привет", "Хауди", "Какие люди? Это же", "Хеллоу"]
#
# if config.greetingsD is not True:
#     print(random.choice(hellower) + ", " + config.name + "!")
# else:
#     if dt.now().hour >= 4 and dt.now().hour <= 12:
#         print(greeting[0] + ", " + config.name + "!")
#     elif dt.now().hour >= 12 and dt.now().hour <= 16:
#         print(greeting[1] + ", " + config.name + "!")
#     elif dt.now().hour >= 16 and dt.now().hour <= 24:
#         print(greeting[2] + ", " + config.name + "!")
#     elif dt.now().hour >= 0 or dt.now().hour <= 4:
#         print(greeting[3] + ", " + config.name + "!")

# def settings():
#     print("Ник:", config.name)
#     if config.greetingsD is True:
#         print("Стиль приветствия: Деловой")
#     else:
#         print("Стиль приветствия: Разговорный")
#
#     while True:
#         change = input("Желаете ли вы что-нибудь изменить?\n> ")
#         if change == "Нет":
#             break
#         elif change == "Да":
#             while True:
#                 ch = input("Что вы хотите изменить?\n> ")
#                 if ch == "Ник":
#                     setting.setname()
#                     break
#                 elif ch == "Стиль приветствия":
#                     setting.setgreeting()
#                     break
#         else:
#             print("Я вас не понял. Здесь нужно написать Да или Нет.")
#
# def now_track():
#     client = Client("AQAAAAAiZU9XAAG8Xh_RpJGGeEgykU-j-pwEGWk").init()
#
#     queues = client.queues_list()
#     last_queue = client.queue(queues[0].id)
#
#     last_track_id = last_queue.get_current_track()
#     last_track = last_track_id.fetch_track()
#
#     artists = ', '.join(last_track.artists_name())
#     title = last_track.title
#     fsec = last_track.duration_ms // 1000 % 60
#     print(f'Сейчас играет: {artists} - {title}')
#     print("Длина трека: " + str(last_track.duration_ms // 60000) + ":" + str(int(fsec//10)) + str(int(fsec%10)))

if __name__ == '__main__':
    executor.start_polling(dp)