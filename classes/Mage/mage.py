from classes.base_class import BasicCombat
from classes.spellcasting import Spellcaster

class Mage(BasicCombat, Spellcaster):
    def __init__(self, name):
        BasicCombat.__init__(self, name, hp=12, ac=12, attack_bonus=1)
        Spellcaster.__init__(self)
        self.class_name = "Mage"
        self.abilities["Basic Attack"] = {
            "Damage": "1d6",
            "Description": "A simple magical attack"
        }

        # Tilføj spells
        self.add_spell("Fireball", "1d10", "A fiery blast of magic")
        self.add_spell("Ice Shard", "1d8", "A shard of ice that can freeze enemies")
