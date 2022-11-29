import os
import random
from hero_engine import *
from main import *

"""
todo: вывести какие предметы забрали
"""
"""
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

"""

def combat(hero):
    enemy = make_hero(damage=0, xp_now=1000000, inventory=["орочий меч", "конь"])
    enemy_damage = enemy[8]
    hero_damage = hero[8]
    while hero[2] > 0 and enemy[2] > 0:
        print(f"Вас встретил {enemy[0]} ")
        print(f"Жизни {enemy[0]} :{enemy[2]}")
        print("Ваши жизни", hero[2])
        print(f"Зелья: {hero[9]}")
        print("""
        1-Cражаться
        2-Использовать зелье""")
        choice_1=input("Что делать будем?: ")
        os.system("cls")
        if choice_1 == "1":
                hero[2] = hero[2] - enemy_damage
                enemy[2] = enemy[2] - hero_damage
                print(f"{hero[0]} нанес: ", hero_damage)
                print(f"{enemy[0]} нанес вам:", enemy_damage)
                input("Нажмите ENTER что бы продолжить")
                os.system("cls")
                if hero[2] == 0 or hero[2] < 0:
                    input("Вы проиграли")
                    break

                if enemy[2] == 0 or enemy[2] < 0:
                    print(f"Вы победили и получили {enemy[3]} опыта")
                    input("Нажмите ENTER чтобы продолжить")
                    system("cls")
                    combat_result(hero, enemy)
                    
        elif choice_1 == "2" and hero[9] > 0:
                hero[9] -= 1
                hero[2] += 10
                if hero[2]>hero[1]: hero[2] = hero[1]
                input("Нажмите ENTER что бы продолжить")
        elif choice_1 == "2" and hero[9] < 0:
            print("недостаточно зелий")
            input("Нажмите ENTER что бы продолжить")

def combat_result(hero, enemy):
    print(f"получил {enemy[3]} опыта")
    print(f"получил {enemy[7]} денег")
    print(f"забирает предметы ")
    hero[3] += enemy[3]
    hero[7] += enemy[7]
    hero[10] += enemy[10]
    level_up(hero)
    show_hero(hero)
