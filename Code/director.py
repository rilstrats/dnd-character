from typing import List
from dice import Dice
from ability import Ability
# from search import SearchSpecific
import constants

class Director():
    def __init__(self):
        self.prepare_dice_bag()
        self.prepare_abilties()

    def prepare_dice_bag(self):
        self.dice_bag = {}
        for sides in constants.DICE_OPTIONS:
            name = "d" + str(sides)
            self.dice_bag[name] = Dice(name, sides)

    def prepare_abilties(self):
        self.standard_array = constants.STANDARD_ARRAY
        self.abilities = {}
        for ability, score in constants.ABILITY_OPTIONS:
            # search_object = SearchSpecific(ability["url"])
            self.abilities[ability] = Ability(score, ability)

    def roll_user_dice(self):
        user_dice = input("Which dice would you like to roll? ")
        try:
            print(self.dice_bag[user_dice].roll())
        except:
            print("Please choose a valid dice option.")