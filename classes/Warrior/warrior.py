from classes.base_class import BasicCombat, roll_damage

class Warrior(BasicCombat):
    def __init__(self, name):
        super().__init__(name, hp=20, ac=15, attack_bonus=2)
        self.class_name = "Warrior"
        self.abilities["Power Strike"] = {
            "Damage": "1d8",
            "Description": "A powerful strike for extra damage"
        }

    def power_strike(self, target):
        print(f"{self.name} uses Power Strike!")
        dmg = roll_damage("1d8")
        target.take_damage(dmg)
