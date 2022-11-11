import os
import shop #импортируем shop.py
import shaman #импортируем shaman.py
import battle #импортируем battle.py
import random #импортируем модуль random



def show_menu():
    """
    показ главного меню

    из него начинается игра или заканчивается программа
    TODO:
        сохранение/загрузка
        настройки: цвет текста

    """

    #главный цикл меню
    while True:
        os.system("cls")
        print("1-Начать новую игру")
        print("2-Выйти")
        answer = input("Номер ответа: ")
        if answer == "1":
            make_hero()
            break
        elif answer == "2":
            print('Выхожу')
            break
    print("Выходим из меню.Пока.")





def create_main_char():
    input



def start_game(player):
    '''
    начинает игру
    принимает значения из create_char
    '''

    #цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        print(f"Имя: {player[0]}")
        print(f"Жизни: {player[1]}")
        print(f"Опыт: {player[2]}")
        print(f"Деньги: {player[3]}")
        print(f"Урон: {player[4]}")
        print(f"Зелья {player[5]}")
        input("Нажмите ENTER для продолжения")
        os.system("cls")
        print(f"""
            {player[0]} оказывается у камня
        1 - Поехать на битву с разбойниками
        2 - Поехать к шаману
        3 - Поехать в лавку алхимика
            """)
        choice = input("Куда поедем ?: ")
        if choice == "1":
            print("Поехал к разбойникам")
            battle.encounter(player)

        elif choice == "2":
            print("Поехал к шаману")
            shaman.shaman_game(player)

        elif choice == "3":
            print("Поехал к алхимику")
            player = shop.shop(player)



show_menu()


