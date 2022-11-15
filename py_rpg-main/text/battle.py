import os
import random
import hero_engine



# name, hp, xp, money, damage, potion
def encounter(player, enemy):
    in_battle = True
    robber_name = enemy[0]
    robber_hp = enemy[1]
    robber_damage = enemy[4]
    player_name = player[0]
    player_hp = player[1]
    player_xp = player[2]
    player_damage = player[4]
    player_potion = player[5]
    
    

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
                #player_name, player_hp, player_xp, player_money, player_damage, player_potion

                if robber_hp == 0 or robber_hp < 0:
                    player_xp += 10
                    print("Вы победили и получили 10 опыта")
                    input("Нажмите ENTER чтобы продолжить")
                    return player[0], player_hp, player_xp, player[3], player[4], player_potion
        elif choice_1 == "2" and player_potion > 0:
                player_potion -= 1
                player_hp += 15
                print("Использовал зелье и восстановил 15 жизней")
                input("Нажмите ENTER что бы продолжить")
        elif choice_1 == "2" and player_potion < 0:
            print("недостаточно зелий")
            input("Нажмите ENTER что бы продолжить")
