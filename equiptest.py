from random import randint
import os


# TODO: Красивое отображение предметов в инвентаре и в момент выбора


def make_hero(name=None,
              hp_max=None,
              hp_curr=None,
              xp_now=0,
              xp_next=None,
              lvl=1,
              knowleage_points=0,
              money=None,
              damage=None,
              inventory=None,
              armor_slot=None,
              weapon_slot=None) -> dict:
    """
    занимается создание персонажа(игрока или врага)
    """
    if not name:
        name = "Тест"
    if not hp_max:
        hp_max = randint(1, 100)
    if not hp_curr:
        hp_curr = hp_max
    if not xp_next:
        xp_next = 468 * (lvl ** 2)
    if not xp_now:
        xp_now = 0
    if not money:
        money = randint(1, 100)
    if not damage:
        damage = randint(1, 3)
    if not inventory:
        inventory = []
    if not armor_slot:
        armor_slot = []
    if not weapon_slot:
        weapon_slot = []

    hero = {"Имя": name,
            "Максимум хп": hp_max,
            "Текущее хп": hp_curr,
            "Текущий xp": xp_now,
            "Xp до след.уровня": xp_next,
            "Уровень": lvl,
            "Очки мудрости": knowleage_points,
            "Деньги": money,
            "Урон": damage,
            "Инвентарь": inventory,
            "Броня": armor_slot,
            "Оружие": weapon_slot
            }
    return hero


def show_hero(hero: dict):
    """
    показывает героя
    """
    print("")
    for key, val in hero.items():
        print(f"{key}:{val}")


def consume_item(hero: dict, item: dict) -> None:
    """
    проверяет класс предмета типа "consumable"
    в зависимости от класса использует предмет
    """
    if item["класс"] == "зелье":
        if item["имя"] == "Зелье лечения":
            print("Использовал зелье лечения")
            hero["Текущее хп"] += 10
            input("Нажмите ENTER чтобы продолжить")
        if item["имя"] == "Зелье опыта":
            print("Использовал зелье опыта")
            hero["Текущий xp"] += 100
            input("Нажмите ENTER чтобы продолжить")
    elif item["класс"] == "еда":
        print("Использовал еду")


def show_item(item: dict):
    """
    отображение предмета
    """
    if item:
        if item['модификатор'] >= 0:
            print(f"название: {item['имя']}",
                  f"тип: {item['тип']}",
                  f"модификатор: +{item['модификатор']}",
                  f"цена продажи: {item['цена продажи']}")
        else:
            print(f"название: {item['имя']}",
                  f"тип: {item['тип']}",
                  f"модификатор: -{item['модификатор']}",
                  f"цена продажи: {item['цена продажи']}")


def generate_item(name: str,
                  type: str,
                  modifier: int,
                  klass: str,
                  sell_price: int) -> dict:
    """
    занимается созданием предметов
    """
    item = {"имя": name,
            "тип": type,
            "модификатор": modifier,
            "класс": klass,
            "цена продажи": sell_price}
    return item


def equip_item(item: dict, otkuda: list, kuda: list) -> None:
    """
    проверяет наличие предмета в слоте
    экипирует предмет в слот
    если в слоте уже есть предмет меняет местами экипируемый предмет и экипированный
    """
    if len(kuda) >= 1:
        otkuda.append(kuda[0])
        kuda.pop(0)
        kuda.append(item)
        otkuda.remove(item)
    else:
        kuda.append(item)
        otkuda.remove(item)


def use_item(hero: dict, item: dict) -> None:
    """
    проверяет тип предмета
    в зависимости от типа предмета использует к предмету соответствующую функцию
    """
    if item["тип"] == "armor":
        equip_item(item, hero["Инвентарь"], hero["Броня"])
    elif item["тип"] == "sword":
        equip_item(item, hero["Инвентарь"], hero["Оружие"])
    elif item["тип"] == "consumable":
        consume_item(hero, item)
    else:
        print("Не удалось использовать предмет")


def show_inventory(hero: list) -> None:
    '''
    нужна для показа инвентаря кого-либо(игрок/враг)
    '''
    for item in enumerate(hero["Инвентарь"]):
        print(item)


def choose_option(hero: list, options: list) -> int:
    """
    показывает варианты
    получает ввод  пользователя
    проверяет ввод пользователя и возвращает его если он есть в вариантах
    """
    choosen_option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        choosen_option = int(choosen_option)
    except ValueError:
        print("Ввод должен быть целым числом и не должен быть отрицательным")
        return choose_option(hero, options)
    else:
        if choosen_option < len(options) and choosen_option > -1:
            return choosen_option
        else:
            print("недопустимое число")
            return choose_option(hero, options)


def show_options(hero: list, options: list) -> None:
    """
    показывает варианты для выбора
    """
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def inventory_test(hero):
    """
    проверка всех функций инвентаря
    """
    options = ["Использовать предмет", "Выйти"]
    show_hero(hero)
    print(" ")
    show_options(hero, options)
    first = choose_option(hero, options)
    os.system("cls")
    if first == 0:
        show_inventory(hero)
        print("Что использовать?")
        item = choose_option(hero, hero["Инвентарь"])
        use_item(hero, hero["Инвентарь"][item])
    else:
        print("Выходим...")


armor = generate_item("Броня из кожи дракона", 'armor', 9999, "броня", 1000)
armor1 = generate_item("Броня не из кожи дракона", 'armor', 1, "броня", 1000)
sword = generate_item("Меч всем головы отсечь", 'weapon', 9999, "меч", 1000)
potion = generate_item("Зелье лечения", "consumable", 10, "зелье", 1000)

player = make_hero(inventory=[armor, sword, potion], armor_slot=[armor1])
inventory_test(player)
show_hero(player)
