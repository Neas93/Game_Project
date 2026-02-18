from classes.Warrior.warrior import Warrior
from classes.base_class import roll_damage

class Barbarian(Warrior):
    def __init__(self, name):
        super().__init__(name)  # arver HP, AC, attack_bonus og Power Strike
        self.class_name = "Barbarian"
        self.raging = False  # Rage-status

        # Barbarian-specifik evne
        self.abilities["Rage"] = {
            "Damage": "Extra 1d6 for 3 turns",
            "Description": "Enter a furious rage, dealing extra damage"
        }

    def start_rage(self):
        if not self.raging:
            print(f"{self.name} enters a Rage!")
            self.raging = True
        else:
            print(f"{self.name} is already raging!")

    def end_rage(self):
        if self.raging:
            print(f"{self.name}'s Rage ends.")
            self.raging = False

    def rage_attack(self, target):
        # Rage giver ekstra damage
        if not self.raging:
            print(f"{self.name} is not raging! Using normal attack instead.")
            self.basic_attack(target)
            return
        
        print(f"{self.name} uses Rage Attack!")
        dmg = roll_damage("1d6") + roll_damage("1d6")  # ekstra d6 i rage
        target.take_damage(dmg)
