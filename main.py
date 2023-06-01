import random, config, sys, os, wikipedia
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import requests as r
from yandex_music import Client
from fuzzywuzzy import fuzz, process
from aiogram import Bot, types
from phonenumbers import parse, geocoder, timezone, carrier
from phonenumbers.phonenumberutil import NumberParseException
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import mark as btn
# from transliterate import translit
from googletrans import Translator


bot = Bot(config.token)
dp = Dispatcher(bot)
translator = Translator()


# Bot variables
emojies =['⭐', '❤️', '🔥', '✨', '👨‍💻', '👨‍🔧']
errors = ['Я не понял! Напиши что-то менее остроумное.', "Моя твоя не понимать! Пиши понятнее.", "Ошибка: БотСлишкомТупойЧтобыЭтоПонять!", "Ничего не понимаю!", "Сорри", "май брейн ис туу смол ту андерстенд тхис!"]
greeting = ["Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи"]
weather_cmds = ["погода", "температура"]
jokes_list_start_num = 0
version = "0.0.4"
build = "Альфа"

# User commands
user_greet = ['Привет', "Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи", "Аве", "Салам", "Привет", "Хауди", "Хеллоу"]
jokes_cmds = ["Анекдот", "Шутка", "Прикол"]
all_cmds = [*jokes_cmds, *user_greet, "О боте", "Настройки", "кубик"]

# Bot commands
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    global emojies
    name = message.from_user.first_name
    #await bot.send_message(message.from_user.id, "text=message.from_user.id)
    if 4 <= dt.now().hour <= 12:
        if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
            await bot.send_message(message.from_user.id, text=f"{greeting[0]}, {name}!")
        else:
            await bot.send_message(message.from_user.id, text=f"{greeting[0]}, {name}! " + random.choice(emojies))
    elif 12 <= dt.now().hour <= 16:
        if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
            await bot.send_message(message.from_user.id,text=f"{greeting[1]}, {name}!")
        else:
            await bot.send_message(message.from_user.id, text=f"{greeting[1]}, {name}! " + random.choice(emojies))
    elif 16 <= dt.now().hour <= 24:
        if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
            await bot.send_message(message.from_user.id, text=f"{greeting[2]}, {name}!")
        else:
            await bot.send_message(message.from_user.id, text=f"{greeting[2]}, {name}! " + random.choice(emojies))
    elif dt.now().hour >= 24 or dt.now().hour <= 4:
        if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
            await bot.send_message(message.from_user.id, text=f"{greeting[3]}, {name}!")
        else:
            await bot.send_message(message.from_user.id, text=f"{greeting[3]}, {name}! " + random.choice(emojies))
    # if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
    #     await bot.send_message(message.from_user.id, "text=f"{greeting[3]}, "{name}!")
    # else:
    #     await bot.send_message(message.from_user.id, "text=f"{greeting[3]}, "{name}!" + random.choice(emojies))

# Bot chat-commands

@dp.message_handler(content_types=['text'])
async def all_textes(message: types.Message):
    global errors, last_jokes, jokes_list_start_num, greeting, emojies, version
    name = message.from_user.first_name

    if fuzz.partial_ratio(message.text, jokes_cmds) > 65:
        url = 'https://www.anekdot.ru/release/anekdot/day/'
        html = r.get(url)
        soup = bs(html.text, 'html.parser')
        await bot.send_message(message.from_user.id, text=soup.select(".text")[jokes_list_start_num].text)
        jokes_list_start_num += 1
    elif fuzz.ratio(message.text, 'О боте') > 65:
        await message.answer(f'<i>Project Epsilon (ε)</i>\nВерсия: <i>{version}</i>\nСборка: <i>{build}</i>\nРазработчики: <i>@notCloffer, @DimaEmelianov90</i>', parse_mode="HTML")
    elif fuzz.ratio(message.text, user_greet) > 65:
        if 4 <= dt.now().hour <= 12:
            if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
                await message.reply(f"{greeting[0]}, {name}!")
            else:
                await bot.send_message(message.from_user.id, text=f"{greeting[0]}, {name}! " + random.choice(emojies))
        elif 12 <= dt.now().hour <= 16:
            if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
                await message.reply(f"{greeting[1]}, {name}!")
            else:
                await bot.send_message(message.from_user.id, text=f"{greeting[1]}, {name}! " + random.choice(emojies))
        elif 16 <= dt.now().hour <= 24:
            if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
                await message.reply(f"{greeting[2]}, {name}!")
            else:
                await bot.send_message(message.from_user.id, text=f"{greeting[2]}, {name}! " + random.choice(emojies))
        elif dt.now().hour >= 24 or dt.now().hour <= 4:
            if int(message.from_user.id) != int("1618502708") and int(message.from_user.id) != int("940369449"):
                await message.reply(f"{greeting[3]}, {name}!")
            else:
                await bot.send_message(message.from_user.id, text=f"{greeting[3]}, {name}! " + random.choice(emojies))
        # print(fuzz.ratio(message.text, user_greet))
    elif fuzz.ratio(message.text, 'Настройки') > 65:
        await bot.send_message(message.from_user.id, text="Данная функция разрабатывается пожоди!")
    elif message.text.startswith("+7"):
        mts_codes = ("901", "902", "904", "908", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "950", "958", "978", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989")

        parsrnum = parse(message.text)
        timeZone = timezone.time_zones_for_number(parsrnum)
        Karri = carrier.name_for_number(parsrnum, 'ru')
        Region = geocoder.description_for_number(parsrnum, 'ru')

        if '993' in message.text or '995' in message.text:
            Karri = "Тинькофф Мобайл"
        elif message.text[2:-7] in mts_codes:
            Karri = "МТС"
        # print(message.text[2:-7])
        await message.reply(f'Страна: <i>{Region}</i>\nОператор: <i>{Karri}</i>', parse_mode="HTML")
        # \nВременная зона: < i > {timeZone} < / i >\n
    elif fuzz.partial_ratio(message.text, "кубик") > 65:
        await message.answer_dice()
    elif message.text not in all_cmds:
        wiki = message.text
        wikipedia.set_lang("ru")
        title = wikipedia.page(wiki).title
        page = wikipedia.summary(wiki)
        await message.reply(f"<strong><i>{title}</i></strong>\n\n{page}", parse_mode='HTML')
    elif fuzz.ratio(message.text, weather_cmds) > 65:
        await message.reply("Напиши название города", reply_markup=btn.WeatherMenu)
    else:
        await bot.send_message(message.from_user.id, text=random.choice(errors))

@dp.message_handler(content_types=["location"])
async def location(message):
    if message.location is not None:
        global translator
        # print(message.location)
        w = r.get(f"https://api.openweathermap.org/data/2.5/weather?lat={message.location.latitude}&lon={message.location.longitude}&appid={config.api_code}")

        req = w.json()
        # print(req)

        city = req["name"]
        temp = req["main"]['temp'] 
        humidity = req["main"]["humidity"]
        pressure = req["main"]["pressure"]
        wind = req["wind"]["speed"]
        result = translator.translate(city, dest='ru').text
        deletter = types.ReplyKeyboardRemove()
        await message.reply(
            f"В городе: {result}\nТемпература: {round(temp-273.15)} C°\nВлажность: {humidity} % \nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с", reply_markup=deletter)


if __name__ == '__main__':
    executor.start_polling(dp)