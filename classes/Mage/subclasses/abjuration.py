from classes.Mage.mage import Mage

class Abjuration(Mage):
    def __init__(self, name):
        super().__init__(name)  # arver HP, AC, attack_bonus og Mage-spells
        self.class_name = "Abjuration"

        # Abjuration-specifikke abilities
        self.abilities["Shield Ward"] = {
            "Damage": "0",
            "Description": "Raises AC temporarily to block attacks"
        }
        self.abilities["Protective Aura"] = {
            "Damage": "0",
            "Description": "Grants a buff to allies’ AC or resistances"
        }

    def shield_ward(self):
        print(f"{self.name} casts Shield Ward! AC increased temporarily")
        self.ac += 2  # midlertidig buff
        # man kan senere tilføje turns/countdown for hvor længe buffen varer

    def protective_aura(self):
        print(f"{self.name} activates Protective Aura!")
        # Placeholder: kan bruges til allies senere
