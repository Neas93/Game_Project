class Warrior:
    def __init__(self):
        self.class_name = "Warrior"
        self.hp = 100
        self.resource_name = "Rage"
        self.resource_amount = 50

        self.abilities = {
            "Whirlwind": {"damage": 50, "target": "AOE", "cost": 15},
            "Bash": {"damage": 15, "target": "Single target", "cost": 10},
            "Heroic Strike": {
                "damage": 15,
                "target": "Single target",
                "cost": 0,
                "rage_generation": 15
            }
        }
