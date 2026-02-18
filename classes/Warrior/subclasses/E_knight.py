from classes.Warrior.warrior import Warrior
from classes.spellcasting import Spellcaster

class EldritchKnight(Warrior, Spellcaster):
    def __init__(self, name):
       
        Warrior.__init__(self, name)
        Spellcaster.__init__(self)
        self.class_name = "Eldritch Knight"
        
        
        self.add_spell("Magic Missile", "1d6", "A magic bolt that always hits")
        self.add_spell("Shield Spell", "0", "Raises AC temporarily")
        
        self.abilities["Sword Slash"] = {
            "Damage": "1d8",
            "Description": "A powerful sword strike"
        }
