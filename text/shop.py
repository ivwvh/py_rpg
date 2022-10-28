def shop(player_money,player_name,player_hp,player_xp, player_potion):
    os.system("cls")
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
    if answer == "1":
        player_potion += 1
        player_money -= 10

    input("-----------------")
