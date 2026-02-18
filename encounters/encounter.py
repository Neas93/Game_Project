from characters.enemy1 import Enemy

def encounter(player):
    print("\nA wild Goblin appears!")
    enemy = Enemy(name="Goblin", hp=12, ac=12, attack_bonus=1)

    while enemy.is_alive() and player["class"].hp > 0:
        print("\n--- Choose Action ---")
        print("1. Basic Attack")
        print("2. Use Ability")
        choice = input("Action: ")

        if choice == "1":
            player["class"].basic_attack(enemy)
        elif choice == "2":
            abilities = list(player["class"].abilities.keys())
            if not abilities:
                print("No abilities available!")
                continue

            print("\nChoose ability:")
            for i, a in enumerate(abilities, start=1):
                print(f"{i}. {a}")
            a_choice = input("Ability: ")
            try:
                ability_name = abilities[int(a_choice)-1]
                ability_func = getattr(player["class"], ability_name.lower().replace(" ", "_"), None)
                if ability_func:
                    ability_func(enemy)
                else:
                    print(f"{ability_name} used (no function yet)")
            except:
                print("Invalid choice!")
        else:
            print("Invalid choice!")
            continue

        # Enemy counterattack
        if enemy.is_alive():
            enemy.basic_attack(player["class"])

    if player["class"].hp <= 0:
        print("You were defeated...")
    else:
        print(f"{enemy.name} is defeated! You win!")
