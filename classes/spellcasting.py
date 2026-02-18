from classes.base_class import roll_damage

class Spellcaster:
    def __init__(self):
        self.spells = {}  # dictionary: spell_name -> info

    def add_spell(self, name, damage, description):
        self.spells[name] = {
            "Damage": damage,
            "Description": description
        }

    def cast_spell(self, spell_name, target):
        if spell_name in self.spells:
            dmg = roll_damage(self.spells[spell_name]["Damage"])
            print(f"{self.__class__.__name__} casts {spell_name} for {dmg} damage!")
            target.take_damage(dmg)
        else:
            print(f"{spell_name} is not a known spell!")
