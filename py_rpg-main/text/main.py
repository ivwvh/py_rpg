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
            create_char()
            break
        elif answer == "2":
            print('Выхожу')
            break
    print("Выходим из меню.Пока.")


def create_char():
    '''
     создает персонажа:
        player_money-деньги,
        player_name-имя
        player_hp-жизни, >= 0 иначе проигрышь
        player_xp-опыт, изначально 0
    '''
    player_money = 100
    player_name = input("Введите имя")
    if not player_name:
        player_name = "Илья"
    player_hp = 150
    player_xp = 0
    player_potion = 10
    player_damage = random.randint(1,10)
    input("Нажмите Enter что бы начать игру")
    start_game(player_money,player_name,player_hp, player_xp, player_potion, player_damage)


def start_game(player_money,player_name,player_hp, player_xp, player_potion, player_damage):
    '''
    начинает игру
    принимает значения из create_char
    '''

    #цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        print(f"Имя: {player_name}")
        print(f"Жизни: {player_hp}")
        print(f"Опыт: {player_xp}")
        print(f"Деньги: {player_money}")
        print(f"Урон: {player_damage}")
        print(f"Зелья {player_potion}")
        input("Нажмите ENTER для продолжения")
        os.system("cls")
        print(f"""
            {player_name} оказывается у камня
        1 - Поехать на битву с разбойниками
        2 - Поехать к шаману
        3 - Поехать в лавку алхимика
            """)
        choice = input("Куда поедем ?: ")
        if choice == "1":
            print("Поехал к разбойникам")
            battle.encounter(player_money, player_name, player_hp, player_xp, player_potion, player_damage)

        elif choice == "2":
            print("Поехал к шаману")
            shaman.shaman_game(player_money,player_name,player_hp,player_xp, player_potion)

        elif choice == "3":
            print("Поехал к алхимику")
            shop.shop(player_money,player_name,player_hp,player_xp, player_potion)



show_menu()


