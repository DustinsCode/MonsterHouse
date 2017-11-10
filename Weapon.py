import random

class Weapon():

    def __init__(self):
        self.attMod = random.randint(1,5)
        self.attMod = str('.' + self.attMod)
        self.attMod = float(self.attMod)
        
