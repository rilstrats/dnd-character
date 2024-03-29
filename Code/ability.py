"""
This abstract class can represent any ability.

OOP Principles Used:
    Encapsulation:
        The majority of this information is hidden (_variable_name) and all necessary information can be accessed by using getters and setters.
    Abstraction:
        All you have to do is pass in a name and score, and it can represent any ability (even the optional abilities in the Dungeon Master's Guide)
    Polymorphism:
        All ability scores will be stored in a dictionary so they can be called polymorphically
"""

class Ability():
    def __init__(self, name, score):
        self.set_score(score)
        # self._search_object = search_object
        self._name = name

    def set_score(self, score):
        self._score = score
        self._modifier = score // 2 - 5
        if self._modifier >= 0:
            self._modifier_string = "+" + str(self._modifier)
        elif self._modifier < 0:
            self._modifier_string = str(self._modifier)

    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score

    def get_mod(self):
        return self._modifier

    def get_mod_string(self):
        return self._modifier_string