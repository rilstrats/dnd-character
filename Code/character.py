"""
This class holds all relevant information to the character.

OOP Principles Used:
    Encapsulation:
        The majority of this information is hidden (_variable_name) and all necessary information can be accessed by using getters and setters.
    Polymorphism:
        A for loop is used to create each different ability object.
"""

import constants
import json

from ability import Ability
from helper import Helper

class Character():
    def __init__(self):
        self._helper = Helper()
        self._make_new = self._helper.input_yes_no(prompt="Would you like to create a new character? (YES or NO) ", validating=True)
        if self._make_new == "yes":
            self._create_character()
        elif self._make_new == "no":
            self._load_character()

    def _create_character(self):
        self._name = self._helper.input_string("What is the NAME of your character? (ex: Nyron Starmite) ")
        self._race = self._helper.input_string("What is the RACE of your character? (ex: Half-Elf) ")
        self._class = self._helper.input_string("What is the CLASS of your character? (ex: Paladin) ")
        self._ac = self._helper.input_integer(prompt="What is the AC of your character? ", validating=True, min_number=1, max_number=30)
        self._set_abilties()
        self._set_level(self._helper.input_integer(prompt="What is your character's LEVEL? (between 1 and 20) ", validating=True, min_number=1, max_number=20))
        self._set_hp(self._helper.input_integer(prompt="What is your character's MAX HP? (between 0 and 999) ", validating=True))

        self._save = {
            "name":self._name, 
            "race":self._race, 
            "class":self._class,
            "level":self._level,
            "str":self.abilities["str"].get_score(),
            "dex":self.abilities["dex"].get_score(),
            "con":self.abilities["con"].get_score(),
            "int":self.abilities["int"].get_score(),
            "wis":self.abilities["wis"].get_score(),
            "cha":self.abilities["cha"].get_score(),
            "hp_max":self._hp_max,
            "ac":self._ac
            }
        with open("code/saves/" + self._name + ".json", "w") as outfile:
            json.dump(self._save, outfile)
    
    def _load_character(self):
        save_path = self._helper.input_path(prompt="What is the NAME of the character you want to load? (ex: Nyron Starmite) ", validating=True, prefix="code/saves/", suffix=".json")
        with open(save_path) as outfile:
            self._save = json.load(outfile)
        self._name = self._save["name"]
        self._race = self._save["race"]
        self._class = self._save["class"]
        self._ac = self._save["ac"]
        self._set_abilties(self._save)
        self._set_level(self._save["level"])
        self._set_hp(self._save["hp_max"])

    def _set_abilties(self, save_dict={}):
        self.standard_array = constants.STANDARD_ARRAY
        self.abilities = {}
        for ability in constants.ABILITIES:
            if not save_dict:
                score = self._helper.input_integer(prompt=f"What is your character's {ability.upper()} score? (between 0 and 20) ", validating=True, min_number=0, max_number=20)
            else:
                score = save_dict[ability]
            self.abilities[ability] = Ability(ability, score)

    def _set_level(self, level):
        self._level = level
        self._proficiency = (self._level + 7) // 4

    def _set_hp(self, hp_max):
        self._hp_max = hp_max
        self._hp_current = self._hp_max
    
    def get_name(self):
        return self._name

    def get_race(self):
        return self._race

    def get_class(self):
        return self._class

    def get_level(self):
        return self._level

    def get_pro(self):
        return self._proficiency

    def get_hp_max(self):
        return self._hp_max

    def get_hp_current(self):
        return self._hp_current

    def hp_heal(self, amount):
        self._hp_current += amount
        if self._hp_current > self._hp_max:
            self._hp_current = self._hp_max

    def hp_damage(self, amount):
        self._hp_current -= amount
        if self._hp_current < 0:
            self._hp_current = 0

    def get_ac(self):
        return self._ac