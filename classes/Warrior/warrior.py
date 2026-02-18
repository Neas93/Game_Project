from classes.base_class import BaseClass, roll_damage

class Warrior(BaseClass):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 15
        self.ac = 14
        self.strength = 4
        self.class_name = "Warrior"
        self.abilities = {
            "Power Strike": {"damage": "1d8", "description": "Strong attack"}
        }

    def power_strike(self, target):
        dmg = roll_damage("1d8") + self.strength
        print(f"{self.name} uses Power Strike! {target.name} takes {dmg} damage.")
        target.take_damage(dmg)
