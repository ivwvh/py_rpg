from random import randint, choice
from os import system

first_name = ("Жран", "Дрын", "Бряк", "Брысь")
last_name = ("Борзой", "Злобный","Лютый","Зловонный")
"""
TODO:сделать цикл повышения уровня пока текущий опыт превышает нужный для повышения -done-
выбрать какие статы повышать при повышении уровня
"""
'''
[0]name - имя,
[1]hp_max - максимальное кол-во жизней,
[2]hp_curr- текущее кол-во жизней,
[3]xp_now - текущий опыт,
[4]xp_next - опыта до след. уровня,
[5]lvl - текущий уровень,
[6]knowleage_points - очки мудрости, выдаются при повышении уровня и используются для изменения параметров,
[7]money - деньги,
[8]damage - урон,
[9]potion - зелья,

'''
#функция генератор героев
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
    sword = None)->list:

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

    hero = [name, hp_max, hp_curr, xp_now, xp_next, lvl, knowleage_points, money, damage, potion, inventory]
    return hero

#функция показа героев
def show_hero(hero):
    print("Имя", hero[0])
    print("Жизней сейчас:", hero[2], "из", hero[1] )
    print("Xp сейчас: ", hero[3], "из", hero[4])
    print("Уровень", hero[5])
    print("Очки мудрости", hero[6])
    print("Денег", hero[7])
    print("Урон", hero[8])
    print("Зелий", hero[9])
    print("Инвентарь", hero[10])
    print("")
    

#функция повыешния уровня
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



            




#сборка и показ героев
