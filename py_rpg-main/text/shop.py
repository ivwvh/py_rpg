import os  


def buy_item(hero: list, item: str, price: int):
    os.system("cls")
    if hero[7] >= price:
        hero[10].append(item)
        hero[7] -= price
        print(f'Вы купили {item}')
    else:
        print(f"Вам не хватает {price-hero[7]} монет")

    input("\nНажмите ENTER чтобы продолжить")






            




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

