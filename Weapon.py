import random

class Weapon():
	"""
	Weapons for the player to use
	"""

	def __init__(self):
		self.attMod = random.randint(1,5)
		self.attMod = str('.' + self.attMod)
		self.attMod = float(self.attMod)


class HersheyKiss(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Hershey Kiss'

class SourStraw(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Sour Straw'

class ChocolateBar(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Chocolate Bar'

class NerdBomb(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Nerd Bomb'
