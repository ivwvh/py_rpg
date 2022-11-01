import os
import random


def encounter(player_money, player_name, player_hp, player_xp, player_potion, player_damage):
    in_battle = True
    robber_name = "Test"
    robber_hp = 20
    robber_damage = random.randint(1,5)
    print(f"{player_name} подезжает к лагерю разбойников")
    while in_battle:
        print(f"Вас встретил {robber_name} ")
        print(f"Жизни {robber_name} :{robber_hp}")
        print("Ваши жизни", player_hp)
        print(f"Зелья: {player_potion}")
        print("""
        1-Cражаться
        2-Использовать зелье""")
        choice_1=input("Что делать будем?: ")
        os.system("cls")
        if choice_1 == "1":
                player_hp = player_hp - robber_damage
                robber_hp = robber_hp - player_damage
                print(f"{player_name} нанес: ", player_damage)
                print(f"{robber_name} нанес вам: {robber_damage}")
                input("Нажмите ENTER что бы продолжить")
                os.system("cls")
                if player_hp == 0 or player_hp < 0:
                    input("Вы проиграли")
                    break

                if robber_hp == 0 or robber_hp < 0:
                    input("Вы победили")
                    break
        elif choice_1 == "2":
                player_potion -= 1
                player_hp += 15
                print("Использовал зелье и восстановил 15 жизней")
                input("Нажмите ENTER что бы продолжить")
        
