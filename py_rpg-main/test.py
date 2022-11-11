from random import randint, choice

first_name = ("Жран", "Дрын", "Бряк", "Брысь")
last_name = ("Борзой", "Злобный","Лютый","Зловонный")


def make_hero(name=None,
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
    return(name, hp, xp, money, damage, potion)


player = make_hero(name="Вася Питонов", hp=100)
enemy_0 = make_hero()
enemy_1 = make_hero()
enemy_2 = make_hero()
enemy_3 = make_hero()
print (enemy_0 ,enemy_1, enemy_2, enemy_3)