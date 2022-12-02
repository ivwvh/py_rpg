from os import system
from hero_engine import *
from shop import *
from battle import *


def play_dice(hero, bet):
    if bet > 0:
        if bet <= hero[7]:
            hero_score = randint(2, 12)
            casino_score = randint(2, 12)
            print(f"Игрок выбросил: {hero_score},казино выбрасывает: {casino_score} ")
            if hero_score > casino_score:
                hero[7] += bet
                print("Игрок победил")

            elif hero_score < casino_score:
                hero[7] -= bet
                print("казино победило")
            else:
                print("ничья")

        else:
            print("У героя не хватает денег")
    else:
        print("Такая ставка невозможна, Ставки принимаются от 1 монет")


def consume_item(hero: list, idx: int):
    if idx <= len(hero[10]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[10][idx]}\n")
        if hero[10][idx] =="зелье":
            hero[10].pop(0)
            hero[2] += 10
            if hero[2] + 10 > 100:
                hero[2] = hero[1]
        elif hero[10][idx] == "яблоко":
            pass
        else:
            print("")
            hero[12].pop(idx)
    else:
        print("Предмета нет")


def level_up(hero):
    while hero[3]>=hero[4]:
        hero[5] += 1
        hero[6] += 1
        hero[4] = 468 * (hero[5] *2)
    stat_changer(hero)


def stat_changer(hero):
    while hero[6] > 0:
        print(f"Сейчас у вас {hero[6]} очков мудрости") 
        print("Введите 1 что бы поысить максимум жизней")
        print("Введите 2 что бы повысить урон")
        print("Введите 3 что бы выйти")
        stat = input('Выберите характеристику для повышения')

        if stat == "1":
            hero[1] += 10
            hero[2] = hero[1]
            hero[6] -= 1
            input('Максимум здоровья был повышен. Нажмите любую кнопку что бы продолжить')
            system('cls')
            show_hero(hero)
            input("")
            system('cls')

        elif stat == "2":
            hero[8] += 10
            hero[6] -= 1
            input('Урон был повышен. Нажмите любую кнопку что бы продолжить')
            system('cls')
            show_hero(hero)
            input("")
            system('cls') 
        elif stat == "3":
            break


def choose_option(hero: list, text:str, options:list) -> int:
    """
    показывает описание ситуации из которой делается выбор 
    показывает варианты
    получает ввод  пользователя
    проверяет ввод пользователя и возвращает его если он есть в вариантах
    """
    system("cls")
    print(text)
    for num, option in enumerate(options):
        print(f"{num}. {option}")
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    
    try:
        option = int(option)
    except:
        print("Ввод должен быть целым числом и не должен быть отрицательным")
    else:
        if option < len(options) and option > -1:
            return option
        else:
            print("недопустимое число")


def visit_hub(hero):
    text = (f"{hero[0]} приехал к камню.")
    options =[
    'Сыграть в кости на 10',
    'Ехать к разойникам',
    'Ехать в зелье за 10',
    'Выпить употребить первый предмет из инвентаря',
    'Посмотреть героя'
    ]
    option = choose_option(hero, text, option)

    if option == 0:
        play_dice(hero, 10)
    elif option == 1:
        combat(hero)
    elif option == 2:
        buy_item(hero, "зелье", 10)
    elif option == 3:
        consume_item(hero, 0)
    elif option == 4:
        show_hero(hero)
    input('')