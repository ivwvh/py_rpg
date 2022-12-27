from random import *
from os import *



def choose_option(hero: list, options:list) -> int:
    """
    показывает варианты
    получает ввод  пользователя
    проверяет ввод пользователя и возвращает его если он есть в вариантах
    """
    
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    
    try:
        option = int(option)
    except ValueError:
        print("Ввод должен быть целым числом и не должен быть отрицательным")
        return choose_option(hero, options)
    else:
        if option < len(options) and option > -1:
            return option
        else:
            print("недопустимое число")
            return choose_option(hero, options)



def show_options(hero:list, options:list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def show_hero(hero):
    for k, v in hero.items():
        print(f"{k}:{v}")


def make_hero(name=None,
    hp_max = None,
    hp_curr = None,
    xp_now = 0,
    xp_next = None,
    lvl = 1,
    knowleage_points = 0,
    money = None,
    damage=None,
    potion=None,
    inventory = None,
    armor = None,
    sword = None) -> dict:

    if not name:
        name = "Тест"
        hp_max = randint(1,100)
    if not hp_curr:
        hp_curr = hp_max
    if not xp_next:
        xp_next = 468 * (lvl ** 2)
    if not xp_now :
        xp_now = 0
    if not money:
        money = randint(1,100)
    if not damage:
        damage = randint(1,3)
    if not potion:
        potion = randint(1,3)
    if not inventory:
        inventory = []

    hero = {"имя":name,
    "максимум хп":hp_max,
    "текущее хп":hp_curr,
    "текущий xp":xp_now ,
    "xp до след.уровня":xp_next,
    "уровень":lvl ,
    "очки мудрости":knowleage_points,
    "деньги":money,
    "урон":damage,
    "зелье":potion,
    "инвентарь":inventory,
    "броня":armor,
    "меч":sword
    }
    return hero


def visit_hub(hero:list) -> None:
    text = (f"{hero[0]} приехал в Хаб, здесь есть чем заняться")
    options =[
    'Ехать к алхимику',
    'Поехать в таверну',
    'Показать героя',
    'Ехать к разбойникам',
    'Выйти в главное меню'
    ]

    print(text)
    show_hero(hero)

    system("cls")
    if hub_option == 0:
        return(visit_shop(hero))
    elif hub_option == 1:
        return(visit_inn(hero))
    elif hub_option == 2:
        return(show_hero(hero))
    elif hub_option == 3:
        return combat(hero)
    elif hub_option == 4:
        print('ушли в меню')
    input('Нажмите ENTR чтобы продолжить')


def generate_item(name:str, type:str, modifier:int, sell_price:int)->dict:
    item = {"имя": name,
    "тип": type,
    "модификатор": modifier,
    "цена продажи": sell_price}
    return item


def show_item(item:dict):
    if item:
        if item['модификатор'] >= 0:
            print(f"название: {item['имя']}", f"тип: {item['тип']}", f"модификатор: +{item['модификатор']}", f"цена продажи: {item['цена продажи']}" )
        else:
            print(f"название: {item['имя']}", f"тип: {item['тип']}", f"модификатор: -{item['модификатор']}", f"цена продажи: {item['цена продажи']}" )
player = make_hero()
show_hero(player)


