from classes.base_class import BasicCombat, roll_damage

class Mage(BasicCombat):
    def __init__(self, name):
        super().__init__(name, hp=12, ac=12, attack_bonus=1)
        self.class_name = "Mage"
        self.abilities["Fireball"] = {
            "Damage": "1d10",
            "Description": "A fiery blast of magic"
        }

    def fireball(self, target):
        print(f"{self.name} casts Fireball!")
        dmg = roll_damage("1d10")
        target.take_damage(dmg)
