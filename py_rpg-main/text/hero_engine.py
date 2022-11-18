from random import randint, choice

first_name = ("Жран", "Дрын", "Бряк", "Брысь")
last_name = ("Борзой", "Злобный","Лютый","Зловонный")
"""
TODO:сделать цикл повышения уровня пока текущий опыт превышает нужный для повышения
выбрать какие статы повышать при повышении уровня
"""
'''
[0]name=None,
[1]hp_max = None,
[2]hp_curr = None,
[3]xp_now = 0,
[4]xp_next = None,
[5]lvl = 1,
[6]money = None,
[7]damage=None,
[8]potion=None,

'''

def make_hero(name=None,
    hp_max = None,
    hp_curr = None,
    xp_now = 0,
    xp_next = None,
    lvl = 1,
    money = None,
    damage=None,
    potion=None,
    inventory = None)->tuple:

    if not name:
        name = choice(first_name) + " " + choice(last_name)
    if not hp_max:
        hp_max = randint(1,10)
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

    hero = [name, hp_max, hp_curr, xp_now, xp_next, lvl, money, damage, potion, inventory]
    return hero


def show_hero(hero):
    print("Имя", hero[0])
    print("Жизней сейчас:", hero[2], "из", hero[1] )
    print("Xp сейчас: ", hero[3], "из", hero[4])
    print("Уровень", hero[5])
    print("Денег", hero[6])
    print("Урон", hero[7])
    print("Зелий", hero[8])
    print(" ")


def level_up(hero):
    while hero:
        hero[5] += 1
        hero[4] = 468 * (hero[5] *2)# TODO: xp до след уровня считается автоматичски в зависимости от текущего
        print(f"{hero[0]} получил {hero[5]} уровень")






p1 = make_hero(name="Вася")
p2 = make_hero(money = 100)
p3 = make_hero()

show_hero(p1)
show_hero(p2)
show_hero(p3)


'''
[0]name=None,
[1]hp_max = None,
[2]hp_curr = None,
[3]xp_now = 0,
[4]xp_next = None,
[5]lvl = 1,
[6]money = None,
[7]damage=None,
[8]potion=None,

'''
p2[3] += 10000

level_up(p2)

show_hero(p1)
show_hero(p2)
show_hero(p3)
