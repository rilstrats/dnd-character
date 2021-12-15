"""
An abstract class just used for inheritance.

OOP Principles Used:
    Abstraction:
        A simple class that I just use to inherit from.
"""

class Action:
    def execute(self):
        raise NotImplementedError("execute not implemented in superclass")