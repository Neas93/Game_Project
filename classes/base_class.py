import random

# Dice helpers
def roll_d20():
    return random.randint(1, 20)

def roll_damage(dice_str):
    num, die = map(int, dice_str.lower().split("d"))
    return sum(random.randint(1, die) for _ in range(num))

class BasicCombat:
    def __init__(self, name, hp=10, ac=10, attack_bonus=0):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attack_bonus = attack_bonus
        self.abilities = {}          # <-- vigtig
        self.class_name = "Base"     # default

    def basic_attack(self, target):
        roll = roll_d20() + self.attack_bonus
        if roll >= target.ac:
            dmg = roll_damage("1d6")
            target.take_damage(dmg)
            print(f"{self.name} hits {target.name} for {dmg} damage!")
        else:
            print(f"{self.name} misses {target.name}!")

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"{self.name} takes {dmg} damage! Remaining HP: {self.hp}")

    def is_alive(self):
        return self.hp > 0

    def show_stats(self):
        print(f"{self.name} | Class: {self.class_name} | HP: {self.hp} | AC: {self.ac} | Attack Bonus: {self.attack_bonus}")
