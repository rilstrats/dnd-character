from dice.dice import Dice
from character.ability import Ability
from api.search import SearchSpecific
import constants

class Director():
    def __init__(self):
        self.prepare_dice_bag()
        self.prepare_abilties()
        pass

    def prepare_dice_bag(self):
        self.dice_bag = {}
        for sides in constants.DICE_OPTIONS:
            name = "d" + str(sides)
            self.dice_bag[name] = Dice(name, sides)

    def prepare_abilties(self):
        self.abilities = {}
        for (ability, score) in zip(constants.ABILITY_OPTIONS.get_results().values(), constants.ABILITY_SCORES):
            search_object = SearchSpecific(ability["url"])
            index = ability["index"]
            self.abilities[index] = Ability(score, search_object)

director = Director()