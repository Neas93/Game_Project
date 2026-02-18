from classes.Warrior.warrior import Warrior
from classes.Mage.mage import Mage

line = "-----------------------"

classes = {
    "Warrior": Warrior,
    "Mage": Mage
}

def choose_option(options, text):
    while True:
        print(line)
        for option in options:
            print(option)
        print(line)
        choice = input(text).title()
        if choice in options:
            return choice
        else:
            print("Invalid choice! Try again.\n")

def character_creation():
    # Navn
    player_name = input("Enter your character name: ")

    # Vælg class
    print("Choose your class:")
    class_choice = choose_option(classes, "Class: ")
    player_class = classes[class_choice](player_name)

    print(f"\nYou chose {player_class.class_name}")
    print(f"HP: {player_class.hp}")

    print("\nAbilities:")
    for name, info in player_class.abilities.items():
        print(f"\n{name}")
        for key, value in info.items():
            print(f"  {key}: {value}")

    print(line)
    return player_class
