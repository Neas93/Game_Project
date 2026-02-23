# Base classes
from classes.Warrior.warrior import Warrior
from classes.Mage.mage import Mage

# Subclasses
from classes.Warrior.subclasses import Barbarian, EldritchKnight
from classes.Mage.subclasses import Bladesinger, Abjuration

# Races
from races.Human.human import Human
from races.Elf.elf import Elf
from races.Dwarf.dwarf import Dwarf

line = "-----------------------"

# Base classes
classes = {
    "Warrior": Warrior,
    "Mage": Mage
}

# Subclasses
subclasses = {
    "Warrior": {
        "Barbarian": Barbarian,
        "Eldritch Knight": EldritchKnight
    },
    "Mage": {
        "Bladesinger": Bladesinger,
        "Abjuration": Abjuration
    }
}

# Races
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
        print("Invalid choice! Try again.\n")

def character_creation():
    # Vælg race
    print("Choose your race:")
    race_choice = choose_option(races, "Race: ")
    player_race = races[race_choice]()  # instantiate
    print(f"\nYou chose {player_race.race_name}")
    print(f"Racial buff: {player_race.racial_buff}\n")

    # Vælg base class
    print("Choose your class:")
    class_choice = choose_option(classes, "Class: ")
    name = input("Enter your character name: ")
    player_class = classes[class_choice](name)

    # Vælg subclass, hvis der findes nogen
    if class_choice in subclasses:
        print(f"Choose your subclass for {class_choice}:")
        subclass_choice = choose_option(subclasses[class_choice], "Subclass: ")
        player_class = subclasses[class_choice][subclass_choice](name)

    print(f"\nYou chose {player_class.class_name}")
    print(f"HP: {player_class.hp}")
    print("Abilities:", ", ".join(player_class.abilities.keys()))

    return {
        "race": player_race,
        "class": player_class
    }
