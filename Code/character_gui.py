"""
This class is used to set up and controll the GUI. This class uses polymorphism to drastically reduce the amount of buttons and function calls I have to write by hand.

OOP Principles Used:
    Polymorphism:
        Using a for loop I iterated through the ability scores and created two labels and two buttons for each ability score, each button containing a polymorph method call to roll dice based on the ability it is connected to.
        Using a for loop I iterated through all the dice and created four buttons, each containing a polymorph method call to roll the dice the button is assigned to
"""

import constants

from tkinter import *
from tkinter import ttk

class CharacterGUI():
    def __init__(self, character, dice_bag):
        self._character = character
        self._dice_bag = dice_bag

        self.screen = Tk()
        self._frame = ttk.Frame(self.screen, padding=10)
        self._frame.grid()

        self._dnd_name = ttk.Label(self._frame, text=self._character.get_name())
        self._dnd_name.grid(column=0, row=0)

        self._dnd_race = ttk.Label(self._frame, text="Race: " + self._character.get_race())
        self._dnd_race.grid(column=0, row=1)

        self._dnd_class = ttk.Label(self._frame, text="Class: " + self._character.get_class())
        self._dnd_class.grid(column=1, row=0)

        self._dnd_level = ttk.Label(self._frame, text="Level: " + str(self._character.get_level()))
        self._dnd_level.grid(column=1, row=1)

        self._dnd_hp_max = ttk.Label(self._frame, text="HP Max: " + str(self._character.get_hp_max()))
        self._dnd_hp_max.grid(column=1, row=4)

        self._dnd_hp_current = ttk.Label(self._frame, text="HP Current: " + str(self._character.get_hp_current()))
        self._dnd_hp_current.grid(column=1, row=6)

        self._dnd_hp_change = ttk.Label(self._frame, text="HP Change:")
        self._dnd_hp_change.grid(column=1, row=5)

        self._dnd_choice = ttk.Label(self._frame, text="Ability Modifier Choice:")
        self._dnd_choice.grid(column=1, row=11, columnspan=2)
        
        self._dnd_ability = ttk.Entry(self._frame)
        self._dnd_ability.grid(column=1, row=12, columnspan=2)

        self._dnd_amount = ttk.Entry(self._frame)
        self._dnd_amount.grid(column=2, row=5)

        self._dnd_heal = ttk.Button(self._frame, text="Heal", command=self._heal_amount)
        self._dnd_heal.grid(column=2, row=4)


        self._dnd_damage = ttk.Button(self._frame, text="Damage", command=self._damage_amount)
        self._dnd_damage.grid(column=2, row=6)

        self._dnd_ac = ttk.Label(self._frame, text="AC: " + str(self._character.get_ac()))
        self._dnd_ac.grid(column=2, row=0)

        self._dnd_pro = ttk.Label(self._frame, text="Proficiency: " + str(self._character.get_pro()))
        self._dnd_pro.grid(column=2, row=1)

        self._ability_starting_row = 3
        self._prepare_ability_column()

        self._dice_starting_row = 13
        self._prepare_dice_columns()

    def _prepare_ability_column(self):
        self._ability_row = self._ability_starting_row
        for ability in self._character.abilities.values():
            ttk.Label(self._frame, text="").grid(column=0, row=self._ability_row)
            self._ability_row += 1
            ttk.Label(self._frame, text=ability.get_name().upper()).grid(column=0, row=self._ability_row)
            self._ability_row += 1
            ttk.Label(self._frame, text=str(ability.get_score())).grid(column=0, row=self._ability_row)
            self._ability_row += 1
            ttk.Button(self._frame, text=ability.get_mod_string(), command=lambda this_mod=ability.get_mod(): self._dice_bag["d20"].roll(mod=this_mod)).grid(column=0, row=self._ability_row)
            self._ability_row += 1
            ttk.Button(self._frame, text=ability.get_mod_string() + "+PRO", command=lambda this_mod=ability.get_mod(): self._dice_bag["d20"].roll(mod=this_mod, pro=self._character.get_pro())).grid(column=0, row=self._ability_row)
            self._ability_row += 1

    def _prepare_dice_columns(self):
        self._dice_row = self._dice_starting_row
        dice_column = 1
        for dice in self._dice_bag.values():
            ttk.Label(self._frame, text="").grid(column=1, row=self._dice_row)
            self._dice_row += 1
            ttk.Button(self._frame, text=dice.get_name(), command=lambda this_dice=dice: this_dice.roll()).grid(column=dice_column, row=self._dice_row)
            self._dice_row += 1
            ttk.Button(self._frame, text=dice.get_name() + "+PRO", command=lambda this_dice=dice: this_dice.roll(pro=self._character.get_pro())).grid(column=dice_column, row=self._dice_row)
            self._dice_row += 1
            ttk.Button(self._frame, text=dice.get_name() + "+MOD", command=lambda this_dice=dice: this_dice.roll(mod=self._character.abilities[self._get_ability()].get_mod())).grid(column=dice_column, row=self._dice_row)
            self._dice_row += 1
            ttk.Button(self._frame, text=dice.get_name() + "+MOD+PRO", command=lambda this_dice=dice: this_dice.roll(mod=self._character.abilities[self._get_ability()].get_mod(), pro=self._character.get_pro())).grid(column=dice_column, row=self._dice_row)
            self._dice_row += 1

            if self._dice_row > (self._dice_starting_row + 19): 
                dice_column = 2
                self._dice_row = self._dice_starting_row

    def _get_ability(self):
        entry_text = self._dnd_ability.get().lower()
        if entry_text not in constants.ABILITIES:
            print("Error! Please enter a valid ability name! Using 'STR' as the default.")
            return "str"
        else:
            print(f"Using '{entry_text.upper()}' for this roll.")
            return entry_text

    def _get_amount(self):
        amount = self._dnd_amount.get()
        if amount.isnumeric(): return int(amount)
        else: return 0

    def _heal_amount(self):
        self._character.hp_heal(self._get_amount()) 
        self._dnd_hp_current.config(text="HP Current: " + str(self._character.get_hp_current()))

    def _damage_amount(self):
        self._character.hp_damage(self._get_amount()) 
        self._dnd_hp_current.config(text="HP Current: " + str(self._character.get_hp_current()))
