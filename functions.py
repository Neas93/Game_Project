from classes.Warrior.warrior import Warrior
from classes.Mage.mage import Mage

from races.Human.human import Human
from races.Elf.elf import Elf
from races.Dwarf.dwarf import Dwarf

line = "-----------------------"

classes = {
    "Warrior": Warrior,
    "Mage": Mage
}

races = {
    "Human": Human,
    "Elf": Elf,
    "Dwarf": Dwarf
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
    # Vælg race
    print("Choose your race:")
    race_choice = choose_option(races, "Race: ")
    player_race = races[race_choice]()
    print(f"\nYou chose {player_race.race_name}")
    print(f"Racial buff: {player_race.racial_buff}\n")

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
    return {
        "race": player_race,
        "class": player_class
    }
