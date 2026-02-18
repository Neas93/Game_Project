from functions import character_creation
from classes.base_class import BasicCombat

line = "-----------------------"

def main():
    print("Welcome to the DnD Game!")
    player = character_creation()

    # Dummy enemy
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

        if enemy.is_alive():
            enemy.basic_attack(player)
        else:
            print("Enemy defeated!")

    if not player.is_alive():
        print(f"{player.name} has been defeated!")

if __name__ == "__main__":
    main()
