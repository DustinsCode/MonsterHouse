import random

class Weapon():
"""
Weapons for the player to use
"""

    def __init__(self):
        self.attMod = random.randint(1,5)
        self.attMod = str('.' + self.attMod)
        self.attMod = float(self.attMod)
