import constants

from character_gui import CharacterGUI
from dice import Dice
from character import Character

character = Character()
dice = {}
for sides in constants.DICE_OPTIONS:
    name = "d" + str(sides)
    dice[name] = Dice(name, sides)

character_gui = CharacterGUI(character, dice)
character_gui.screen.mainloop()