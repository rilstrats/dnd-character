"""
This class is used to prepare all dice objects.

OOP Principles Used:
    Inheritance:
        This class inherits from the Action class.
    Polymorphism:
        A for loop is used to create each different class of dice.
"""

import constants

from action import Action
from dice import Dice

class PrepareDice(Action):
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self):
        dice = {}

        for sides in constants.DICE_OPTIONS:
            name = "d" + str(sides)
            dice[name] = Dice(name, sides)
            
        return dice