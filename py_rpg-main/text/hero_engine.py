from random import randint, choice

first_name = ("Жран", "Дрын", "Бряк", "Брысь")
last_name = ("Борзой", "Злобный","Лютый","Зловонный")


def main_char():
    player_name = input("Введите имя")
    if not player_name: player_name = "Илья" 
    player_hp = 100
    player_xp = 0
    player_money = 1000
    player_damage = randint(1,10)
    player_potion = 0
    player = player_name, player_hp, player_xp, player_money, player_damage, player_potion
    return player


def make_enemy(name=None,
    hp=None,
    xp=None,
    money=None,
    damage=None,
    potion=None,)->tuple:
    if not name:
        name = f"({choice(first_name)}, {choice(last_name)})"
    if not hp:
        hp = randint(1,10)
    if not xp:
        xp = randint(1,100)
    if not money:
        money = randint(1,100)
    if not damage:
        damage = randint(1,3)
    if not potion:
        potion = randint(1,3)
    enemy = name, hp, xp, money, damage, potion
    return enemy

