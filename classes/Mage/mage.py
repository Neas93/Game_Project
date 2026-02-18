from classes.base_class import BaseClass, roll_damage

class Mage(BaseClass):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 10
        self.ac = 12
        self.strength = 1
        self.class_name = "Mage"
        self.abilities = {
            "Fireball": {"damage": "1d10", "description": "Burns enemy"}
        }

    def fireball(self, target):
        dmg = roll_damage("1d10")
        print(f"{self.name} casts Fireball! {target.name} takes {dmg} damage.")
        target.take_damage(dmg)
