from os import system
from hero_engine import *
from shop import *
from battle import *
"""
FIXME: 18 строка str is not callable
"""
def show_inventory(hero:list)->None:
    '''
    нужна для показа инвентаря кого-либо(игрок/враг)
    '''
    for item in enumerate(hero[10]):
        print(*item)


def combat_turn(attacker:list, defender:list):
   defender[2] -= attacker[8]  


#def visit_cole(hero):
#    enemy = make_hero(damage=0, xp_now=1000000, inventory=["орочий меч", "конь"])
#    show_hero(hero)
#    show_hero(enemy)
#   return combat(hero)


def combat(hero):
    enemy = make_hero(damage=0, xp_now=1000000, inventory=["орочий меч", "конь"])
    show_hero(hero)
    show_hero(enemy)
    while hero[2] > 0 and enemy[2] > 0:
        text='Сражение началось'
        options = ['Ударить',
        'Использовать предмет']
        show_options(hero, options)
        battle_option=choose_option(hero,text)
        system("cls")
        if battle_option == 0:
            combat_turn(hero, enemy)
            combat_turn(enemy, hero)
        print(f'Игрок нанес {hero[8]}')
        print(f'Враг нанес {enemy[8]}') 
        show_hero(hero)
        show_hero(enemy)
        if battle_option == 1:
            print(options)
            consume_item(hero)
    combat_result(hero,enemy)
       

def combat_result(hero, enemy):
    if enemy[2] <= 0: 
        print(f"получил {enemy[3]} опыта")
        print(f"получил {enemy[7]} денег")
        print(f"{hero[0]} забирает предметы: ", end="")

        for item in enemy[10]:
            print(item, end =", ")

        hero[3] += enemy[3]
        hero[7] += enemy[7]
        hero[10] += enemy[10]
        level_up(hero)
        show_hero(hero)
    elif hero[2] <= 0:
        print("Вы проиграли")
        input('Нажмите ENTER чтобы продолжить')
        return visit_hub


def play_dice(hero:list, bet:str)->None:
    try:
        bet = bet(int)
    except ValueError:
        print("Ставка не является числом")
    else:
        if bet > 0:
            if bet <= hero[7]:
                hero_score = randint(2, 12)
                casino_score = randint(2, 12)
                print(f"Игрок выбросил: {hero_score},казино выбрасывает: {casino_score} ")
                if hero_score > casino_score:
                    hero[7] += bet
                    print("Игрок победил")
                    input('Нажмите ENTER чтобы продолжить')

                elif hero_score < casino_score:
                    hero[7] -= bet
                    print("казино победило")
                    input('Нажмите ENTER чтобы продолжить')
                else:
                    print("ничья")
                    input('Нажмите ENTER чтобы продолжить')

            else:
                print("У героя не хватает денег")
                input('Нажмите ENTER чтобы продолжить')
        else:
            print("Такая ставка невозможна, Ставки принимаются от 1 монет")
            input('Нажмите ENTER чтобы продолжить')
    

def consume_item(hero: list):
    show_options(hero, hero[10])
    idx = choose_option(hero, hero[10])
    # TODO: Не засчитывать плохой выбор за ход в бою
    if idx is not None:
        if idx <= len(hero[10]) - 1 and idx > -1:
            print(f"{hero[0]} употребил {hero[10][idx]}\n")
            if hero[10][idx] =="зелье":
                hero[10].pop(idx)
                hero[2] += 10
                if hero[2] + 10 > 100:
                    hero[2] = hero[1]
            elif hero[10][idx] == "зелье опыта":
                hero[2] += 1000
                hero[10].pop(idx)
            else:
                print("Употребил что-то")
                hero[10].pop(idx)
        else:
            print("Предмета нет")
    else:
        pass


def level_up(hero):
    while hero[3]>=hero[4]:
        hero[5] += 1
        hero[6] += 1
        hero[4] = 468 * (hero[5] *2)
    stat_changer(hero)


def stat_changer(hero:list) -> None:
    while hero[6] > 0:
        print(f"Сейчас у вас {hero[6]} очков мудрости") 
        print("Введите 1 что бы поысить максимум жизней")
        print("Введите 2 что бы повысить урон")
        print("Введите 3 что бы выйти")
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
        elif stat == "3":
            return visit_hub(hero)


def choose_option(hero: list, options:list) -> int:
    """
    показывает варианты
    получает ввод  пользователя
    проверяет ввод пользователя и возвращает его если он есть в вариантах
    """
    
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    
    try:
        option = int(option)
    except ValueError:
        print("Ввод должен быть целым числом и не должен быть отрицательным")
        return choose_option(hero, options)
    else:
        if option < len(options) and option > -1:
            return option
        else:
            print("недопустимое число")
            return choose_option(hero, options)


def visit_hub(hero:list) -> None:
    text = (f"{hero[0]} приехал в Хаб, здесь есть чем заняться")
    options =[
    'Ехать к алхимику',
    'Поехать в таверну',
    'Показать героя',
    'Ехать к разбойникам',
    'Выйти в главное меню'
    ]

    print(text)
    show_hero(hero)
    show_options(hero, options)
    hub_option = choose_option(hero, text)

    os.system("cls")
    if hub_option == 0:
        return(visit_shop(hero))
    elif hub_option == 1:
        return(visit_inn(hero))
    elif hub_option == 2:
        return(show_hero(hero))
    elif hub_option == 3:
        return combat(hero)
    elif hub_option == 4:
        print('ушли в меню')
    input('Нажмите ENTR чтобы продолжить')


def show_options(hero:list, options:list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def visit_shop(hero:list) -> None:
    text = (f"{hero[0]} приехал в лавку алхимика. Здесь есть чем заняться")
    options =[
    'Купить зелье лечения за 10 монет',
    'Купить зелье опыта за 30 монет',
    'Выйти из лавки в хаб'
    ]
    show_hero(hero)
    show_options(hero, options)
    shop_option = choose_option(hero, options)
    if shop_option == 1:
        buy_item(hero, "зелье", 10)
        return visit_shop(hero)
    elif shop_option == 2:
        buy_item(hero, "зелье опыта", 30)
        return visit_shop(hero)
    elif shop_option == 3:
        return visit_hub(hero)


def visit_inn(hero:list) -> None:
    text=(f'{hero[0]} заехал в таверну, здесь можно отдохнуть и поиграть в кости')
    options =[
    'Играть в кости',
    'Отдохнуть в таверне',
    'Выйти из таверны в хаб'
    ]
    inn_option = choose_option(hero, text, options)

    if inn_option == 0:
        bet = input("Введите ставку")
        play_dice(hero, bet)
        return visit_inn
    elif inn_option == 1:
        rest(hero, 10)
        return(visit_inn)
    elif inn_option == 2:
        return(visit_hub(hero))


def rest(hero: list, cost: int) -> None:
    hero[7] -= cost
    hero[2] = hero[1]
    print("Вы отдохнули и восстановили себе все здоровье")
    input('Нажмите ENTER чтобы продолжить')


def show_stat(hero, idx):
    pass


def buy_item(hero: list, item: str, price: int):
    os.system("cls")
    if hero[7] >= price:
        hero[10].append(item)
        hero[7] -= price
        print(f'Вы купили {item}')
        return visit_shop(hero)
    else:
        print(f"Вам не хватает {price-hero[7]} монет")

    input("\nНажмите ENTER чтобы продолжить")
