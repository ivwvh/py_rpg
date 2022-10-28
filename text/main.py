import os
import shop #импортируем shop.py


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
            start_game()
            break
        elif answer == "2":
            print('Выхожу')
            break
    print("Выходим из меню.Пока.")


def start_game():
    '''
    начинает игру
    создает персонажа:
        player_money-деньги,
        player_name-имя
        player_hp-жизни, >= 0 иначе проигрыщ
        player_xp-опыт, изначально 0
    '''
    player_money = 100
    player_name = input("Введите имя")
    if not player_name:
        player_name = "Илья"
    player_hp = 150
    player_xp = 0
    #цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        print(f"Имя {player_name}")
        print(f"Жизни {player_hp}")
        print(f"Опыт {player_xp}")
        print(f"Деньги {player_money}")
        input("Нажмите ENTER для продолжения")
        os.system("cls")
        print(f"""
            {player_name} оказывается у камня
        1 - Поехать на битву с разбойниками
        2 - Поехать к шаману
        3 - Поехать в лавку алхимика
            """)
        choice = input("Введите цифру ответа")
        if choice == "1":
            print("Поехал к разбойникам")
        elif choice == "2":
            print("Поехал к шаману")
        elif choice == "3":
            print("Поехал к алхимику")
            shop.shop(player_name,player_money,player_hp,player_xp)



show_menu()


