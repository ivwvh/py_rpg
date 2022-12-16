from random import *


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

    os.system("cls")
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


player = make_hero()
show_hero(player)


