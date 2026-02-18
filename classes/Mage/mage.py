class Mage:
    def __init__(self):
        self.class_name = "Mage"
        self.hp = 80
        self.resource_name = "Mana"
        self.resource_amount = 100

        self.abilities = {
            "Firebolt": {"damage": 25, "target": "Single target", "cost": 10},
            "Frostbolt": {"damage": 25, "target": "Single target", "cost": 10}
        }
