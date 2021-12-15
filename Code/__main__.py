"""

"""

import constants

from action_prepare_game import PrepareGame
from character_gui import CharacterGUI

prepare_game = PrepareGame()
returned_items = prepare_game.execute()

character = returned_items[0]
dice = returned_items[1]

character_gui = CharacterGUI(character, dice)
character_gui.screen.mainloop()