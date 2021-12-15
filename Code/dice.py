"""
The following class is an abstract class that is used to represent dice of all different sizes

OOP Principles Used:
    Abstraction:
        This class is set up so you can pass any name and amount of sides and it will represent that dice, without having to make any other large amount of changes
    Polymorphish:
        All dice objects are stored in a dictionary so they can be called polymorphically
"""

import random

class Dice():
    def __init__(self, name, sides):
        self._name = name
        self._sides = sides

    def roll(self, mod=0, pro=0):
        roll = random.randint(1, self._sides)
        modified_roll = roll + mod + pro
        print(f"You rolled a {self._name} and got a {roll}, which is a modded {modified_roll}.")
        return modified_roll

    def get_name(self):
        return self._name   