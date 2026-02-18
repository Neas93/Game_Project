import random

def roll_damage(dice: str) -> int:
    count, die = map(int, dice.lower().split("d"))
    return sum(random.randint(1, die) for _ in range(count))

class BaseClass:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.ac = 12
        self.attack_bonus = 2
        self.strength = 2
        self.abilities = {}
        self.class_name = "BaseClass"

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage! HP left: {self.hp}")

    def basic_attack(self, target):
        roll = roll_damage("1d20") + self.attack_bonus
        print(f"{self.name} attacks {target.name}! Roll: {roll}")
        if roll >= target.ac:
            dmg = roll_damage("1d6") + self.strength
            print(f"Hit! {target.name} takes {dmg} damage.")
            target.take_damage(dmg)
        else:
            print("Miss!")
