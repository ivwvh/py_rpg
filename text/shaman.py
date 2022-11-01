import random
import os
def shaman_game(player_money, player_name, player_hp, player_xp, player_potion):
    tries = 5
    shaman_event = True
    shamans_number = random.randint(1, 5)
    print(f"{player_name} встречает шамана")
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
                    shaman_event = False
                    print('Вы победили')


    input('Нажмите любую клавишу чтобы выйти')
