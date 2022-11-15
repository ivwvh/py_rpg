import random
import os
def shaman_game(player):
    tries = 5
    shaman_event = True
    shamans_number = random.randint(1, 5)
    xp = player[2]
    money = player[3]
    print(f"{player[0]} встречает шамана")
    print("Правила игры: Шаман загадывает случайное число от одного до пяти, ваша задача угадать какое число он загадал для этого у вас есть 5 попыток") 
    while shaman_event and tries != 0:
        player_guess= int(input("Введите число: "))
        if player_guess != 0 and player_guess <= 5:
                if  player_guess < shamans_number:
                    print("Это число меньше чем я загадал")
                    tries -= 1
                    print(f"Попыток осталось {tries}")
                    input("Нажмите любую клавишу для продолжения")
                    os.system("cls")
                elif player_guess > shamans_number:
                    print("Это число больше того что я загадал")
                    tries -= 1
                    print(f"Попыток осталось {tries}")
                    input("Нажмите любую клавишу для продолжения")
                    os.system("cls")
                else:
                    xp += 10
                    money += 100
                    print('Вы победили')
                    return player[0], player[1], xp, money, player[4], player[5]

#player_name, player_hp, player_xp, player_money, player_damage, player_potion
    input('Нажмите любую клавишу чтобы выйти')
