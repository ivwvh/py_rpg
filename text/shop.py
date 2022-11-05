import os  


def buy_potions(player_potion):
    return player_potion + 1

def pay(player_money):
    return player_money - 10
   


def shop(player_money, player_name, player_hp, player_xp, player_potion):
    os.system("cls")
    in_shop = True
    while in_shop:
        print(f"Имя {player_name}")
        print(f"Жизни {player_hp}")
        print(f"Опыт {player_xp}")
        print(f"Деньги {player_money}")
        print(f"Зелья {player_potion}")
        input("Нажмите ENTER для продолжения")
        print(f"""
                {player_name} оказывается в магазине алхимика
            1 - Купить зелье за 10 монет
            2 - Поехать к камню
                """)
        answer = input("")
        if answer == "1" and player_money > 0:
            player_potion = buy_potions(player_potion)
            player_money = pay(player_money)
            print("Купил одно зелье")
            os.system("cls")
            
        elif answer == "1" and player_money <= 0:
            print("Нет денег")
            
        elif answer == "2":
            print("Поехал к камню")
            in_shop = False





            