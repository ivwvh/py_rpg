import os  


def shop(player:tuple) -> tuple:
    # player = (player_name, player_hp, player_xp, player_money, player_damage, player_potion)
    money = player[3]
    potion = player[5]
    in_shop = True
    while in_shop:
        os.system("cls")
        print(f"Имя: {player[0]}")
        print(f"Жизни: {player[1]}")
        print(f"Опыт: {player[2]}")
        print(f"Деньги: {player[3]}")
        print(f"Урон: {player[4]}")
        print(f"Зелья {player[5]}")
        input("Нажмите ENTER для продолжения")
        print(f"""
                {player[0]} оказывается в магазине алхимика
            1 - Купить зелье за 10 монет
            2 - Поехать к камню
                """)
        answer = input("")
        if answer == "1" and money > 0:
            potion += 1
            money -= 10
            print("Купил одно зелье")
            os.system("cls")
            
        elif answer == "1" and money <= 0:
            print("Нет денег")
            
        elif answer == "2":
            return
            #  (player[0], money, player_hp, player_xp, player_potion, player_damage)
            





            