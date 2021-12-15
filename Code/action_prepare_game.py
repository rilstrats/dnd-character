"""
This class is used to prepare the character and dice objects so they're ready to be used in the GUI

OOP Principles Used:
    Inheritance:
        This class inherits from the Action class.
"""

from action import Action
from action_prepare_character import PrepareCharacter
from action_prepare_dice import PrepareDice

class PrepareGame(Action):
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        preparations = [PrepareCharacter(), PrepareDice()]

        return_items = []
        for prepare in preparations:
            return_items.append(prepare.execute())

        return return_items