from functions import character_creation
from classes.base_class import roll_damage

# Encounter funktion
def encounter(player):
    print("\nA wild Goblin appears!")

    class Enemy:
        def __init__(self):
            self.name = "Goblin"
            self.hp = 12
            self.ac = 12
            self.attack_bonus = 1
            self.abilities = {}

        def take_damage(self, amount):
            self.hp -= amount
            print(f"{self.name} takes {amount} damage! HP left: {self.hp}")

        def is_alive(self):
            return self.hp > 0

        def basic_attack(self, target):
            dmg = roll_damage("1d4") + self.attack_bonus
            print(f"{self.name} attacks {target.name} for {dmg} damage!")
            target.take_damage(dmg)

    enemy = Enemy()

    while enemy.is_alive() and player["class"].hp > 0:
        print("\n--- Choose Action ---")
        print("1. Basic Attack")
        print("2. Use Ability")
        choice = input("Choose action: ")

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

# Main loop
def main():
    print("Welcome to the RPG!")
    player = character_creation()

    while True:
        print("\n--- Main Menu ---")
        print("1. Explore (fight an enemy)")
        print("2. Rest (heal)")
        print("3. Quit")
        choice = input("Choose action: ")

        if choice == "1":
            encounter(player)
        elif choice == "2":
            # Simpelt heal
            player["class"].hp += 5
            print(f"You rest and recover 5 HP. Current HP: {player['class'].hp}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
