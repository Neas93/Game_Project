from functions import character_creation
from classes.base_class import BasicCombat

line = "-----------------------"

def main():
    print("Welcome to the DnD Game!")

    # Opret spiller
    player_info = character_creation()
    player = player_info["class"]
    race = player_info["race"]

    # Dummy enemy til test
    enemy = BasicCombat("Goblin", hp=10, ac=10)
    print("\nA wild Goblin appears!\n")

    while enemy.is_alive() and player.is_alive():
        print(line)
        print("Choose action:")
        print("1. Basic Attack")
        if player.class_name == "Warrior":
            print("2. Power Strike")
        elif player.class_name == "Mage":
            print("2. Fireball")
        print(line)

        action = input("Action: ")

        if action == "1":
            player.basic_attack(enemy)
        elif action == "2":
            if player.class_name == "Warrior":
                player.power_strike(enemy)
            elif player.class_name == "Mage":
                player.fireball(enemy)
        else:
            print("Invalid action!")

        # Enemy angriber tilbage, hvis den lever
        if enemy.is_alive():
            print(f"\n{enemy.name} attacks!")
            enemy.basic_attack(player)
        else:
            print("Enemy defeated!")

        # Vis spillerens HP efter runden
        print(f"\n{player.name} HP: {player.hp}")

    # Resultat
    if not player.is_alive():
        print(f"{player.name} has been defeated!")
    elif not enemy.is_alive():
        print(f"{player.name} wins the fight!")

if __name__ == "__main__":
    main()
