import random

class Dice():
    def __init__(self, name, sides):
        self.name = name
        self._sides = sides

    def roll(self, ablility_modifier=0, proficiency_modifier=0):
        new_roll = random.randint(1, self._sides) + ablility_modifier + proficiency_modifier
        return new_roll