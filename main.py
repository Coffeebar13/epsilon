import os, rich, sys, time
from random import choice
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import requests as r
from rich.progress import Progress

def first_settings():
    cfg = open("config.py", "a+")
    name = input("Как вы хотели чтобы вас назвали?\n> ")
    fin = open("config.py", "rt", encoding="utf8")
    data = fin.read()
    data = data.replace(config.name, name)
    fin.close()
    fin = open("config.py", "wt", encoding="utf8")
    fin.write(data)
    fin.close()
    while True:
        greeting = input("Какой вы хотите выбрать стиль приветствия? Деловой или Разгоровный?\n> ")
        if greeting == "Деловой":
            cfg.write("\ngreetingsD = True")
            break
        elif greeting == "Разговорный":
            cfg.write("\ngreetingsD = False")
            break
        else:
            print("Я не понял")
    clr = input("Какой цвет использовать для ника для приветствия? ")

def gen_plugin_c():
    cfg = open("config.py", "a+")
    cfg.write("name = 'A'")
    cfg.write("\ngreetingsD = True")
    cfg.close()

def gen_plugin_s():
    set = open("setting.py", "a+", encoding="utf-8")
    set.write("import config\n\n")
    set.write("def setname():\n")
    set.write('    name = input("Как вы хотели чтобы вас назвали?\ n> ")\n    fin = open("config.py","rt", encoding="utf8")\n    data = fin.read()\n    data = data.replace(config.name, name)\n    fin.close()\n    fin = open("config.py", "wt", encoding="utf8")\n    fin.write(data)\n    fin.close()')
    set.write("\ndef setgreeting():")
    set.write('\n    while True:\n        greeting = input("Какой вы хотите выбрать стиль приветствия? Деловой или Разгоровный?\ n> ")\n        if greeting == "Деловой":\n            fin = open("config.py", "rt", encoding="utf8")\n            data = fin.read()\n            data = data.replace("greetingsD = False", "greetingsD = True")\n            fin.close()\n            fin = open("config.py", "wt", encoding="utf8")\n            fin.write(data)\n            fin.close()\n            break\n        elif greeting == "Разговорный":\n           fin = open("config.py", "rt", encoding="utf8")\n           data = fin.read()\n           data = data.replace("greetingsD = True", "greetingsD = False")\n           fin.close()\n           fin = open("config.py", "wt", encoding="utf8")\n           fin.write(data)\n           fin.close()\n           break\n        else:\n           print("Я не понял")')
    set.close()

if os.path.exists('config.py') == False:
     gen_plugin_c()
     with Progress() as progress:
         t_gen_C = progress.add_task("[bold green]Генерирую конфиг...", total=100)
         while not progress.finished:
             progress.update(t_gen_C, advance=0.5)
             time.sleep(0.02)
     import config
else:
    import config
    pass

if os.path.exists('setting.py') == False:
     gen_plugin_s()
     with Progress() as progress:
         t_gen_S = progress.add_task("[bold green]Генерирую настройки...", total=100)

         while not progress.finished:
             progress.update(t_gen_S, advance=0.3)
             time.sleep(0.02)
     import setting
else:
    import setting
    pass

if config.name == "A" and config.greetingsD == True:
    first_settings()
    print("[bold pink]Перезапусти меня! ^-^[/bold pink]")
    python = sys.executable
    os.execl(python, python, *sys.argv)

greeting = ["Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи"]
hellower = ["Аве", "Салам", "Привет", "Хауди", "Какие люди? Это же", "Хеллоу"]

if config.greetingsD != True:
    print(choice(hellower) + ", " + config.name + "!")
else:
    if dt.now().hour >= 4 and dt.now().hour <= 12:
        print(greeting[0] + ", " + config.name + "!")
    elif dt.now().hour >= 12 and dt.now().hour <= 16:
        print(greeting[1] + ", " + config.name + "!")
    elif dt.now().hour >= 16 and dt.now().hour <= 0:
        print(greeting[2] + ", " + config.name + "!")
    elif dt.now().hour >= 0 or dt.now().hour <= 4:
        print(greeting[3] + ", " + config.name + "!")

def jokes():
    url = 'https://www.anekdot.ru/release/anekdot/day/'
    html = r.get(url)
    soup = bs(html.text, 'html.parser')
    txt = soup.find(class_="text")
    print(txt.get_text())

def settings():
    print("Ник:", config.name)
    if config.greetingsD == True:
        print("Стиль приветствия: Деловой")
    else:
        print("Стиль приветствия: Разговорный")

    while True:
        change = input("Желаете ли вы что-нибудь изменить?\n> ")
        if change == "Нет":
            break
        elif change == "Да":
            while True:
                ch = input("Что вы хотите изменить?\n> ")
                if ch == "Ник":
                    setting.setname()
                    break
                elif ch == "Стиль приветствия":
                    setting.setgreeting()
                    break
        else:
            print("Я вас не понял. Здесь нужно написать Да или Нет.")

while True:
    qw = input("> ")
    if qw == "Анекдот":
        jokes()
    elif qw == "Настройки":
        settings()