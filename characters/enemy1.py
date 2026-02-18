from classes.base_class import roll_damage

class Enemy:
    def __init__(self, name="Goblin", hp=12, ac=12, attack_bonus=1):
        self.name = name
        self.hp = hp
        self.ac = ac           # <- VIGTIGT!
        self.attack_bonus = attack_bonus
        self.abilities = {}

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage! HP left: {self.hp}")

    def basic_attack(self, target):
        dmg = roll_damage("1d4") + self.attack_bonus
        print(f"{self.name} attacks {target.name} for {dmg} damage!")
        target.take_damage(dmg)
