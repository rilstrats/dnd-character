"""
This class is used to prepare the character object so they're ready to be used in the GUI.

OOP Principles Used:
    Inheritance:
        This class inherits from the Action class.
"""

from action import Action
from character import Character

class PrepareCharacter(Action):
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
        return Character()