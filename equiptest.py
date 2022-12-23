"""
задача: сделать механику экипировки
что нужно: вывести инвентарь героя
           спросить у игрока что экипировать
           перенести предмет из одного списка в другой
           убрать предмет который экипировал игрок из того места откуда он это сделал

примерный вид: игрок выбирает предмет -> перенести предмет из одного списка в другой

"""


def show_inventory(hero:list)->None:
    '''
    нужна для показа инвентаря кого-либо(игрок/враг)
    '''
    for item in enumerate(hero):
        print(*item)


def equip_o_matic3000(otkuda:list, kuda:list)->None:
    show_inventory(list_1)
    idx = int(input("Какой предмет экипировать?: "))
    kuda.append(otkuda[idx])
    otkuda.pop(idx)


list_1 = [{"кожанная броня": 1}, {"конь"}, {"меч": 100}]
list_2 = []


print(list_1)
print(list_2)
input("До экипировки")
equip_o_matic3000(list_1, list_2)

print(list_1)
print(list_2)
input("После экипировки")


