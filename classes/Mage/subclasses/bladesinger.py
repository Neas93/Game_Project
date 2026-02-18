from classes.Mage.mage import Mage
from classes.base_class import roll_damage

class Bladesinger(Mage):
    def __init__(self, name):
        super().__init__(name)  # arver HP, AC, attack_bonus og Mage-spells
        self.class_name = "Bladesinger"

        # Bladesinger specifikke abilities
        self.abilities["Sword Dance"] = {
            "Damage": "1d6 + spell damage",
            "Description": "A melee attack infused with magical energy"
        }
        
        # Ekstra buffs for Bladesinger
        self.abilities["Arcane Agility"] = {
            "Damage": "0",
            "Description": "Adds +1 AC for next turn"
        }

    def sword_dance(self, target):
        print(f"{self.name} uses Sword Dance!")
        # kombiner melee + spell damage
        dmg = roll_damage("1d6") + roll_damage("1d4")  # 1d6 melee + 1d4 magisk
        target.take_damage(dmg)

    def arcane_agility(self):
        print(f"{self.name} activates Arcane Agility! AC increased for next turn")
        self.ac += 1
