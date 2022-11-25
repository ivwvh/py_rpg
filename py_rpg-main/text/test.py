from hero_engine import *
#сборка и показ героев
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
