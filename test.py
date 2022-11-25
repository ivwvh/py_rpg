from hero_engine import *
from shop import *

#сборка и показ героев
'''
p1 = make_hero(name="Вася")
p2 = make_hero(money = 100)
p3 = make_hero()

show_hero(p1)
show_hero(p2)
show_hero(p3)

input('персонажи созданы')
system("cls")


#выдача опыта игроку 2 и вызов функции повышения уровня
p2[3] += 10000
level_up(p2)


#показ героев после изменений
show_hero(p1)
show_hero(p2)
show_hero(p3)
'''



p1=make_hero(hp_curr=10,money=100000)
show_hero(p1)
input("стоп")

"""
todo: анализатор игр в казино, функция боя:обмен ударами
итог боя проигрыш или победа,
победа: опыт от врага, забрать предметы врага в инвентарь героя
проигрыш: закончить игру

"""
for i in range (10000000):
    play_dice(p1, 1)
    show_hero(p1)
    input("стоп")