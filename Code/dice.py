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