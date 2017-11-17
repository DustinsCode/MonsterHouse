import random

class Weapon():
	"""
	Weapons for the player to use
	"""

	def __init__(self):
		self.attMod = 1
		self.useCount = 0


class HersheyKiss(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Hershey Kiss'
		self.useCount = -1
		self.attMod = 1

class SourStraw(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Sour Straw'
		self.attMod = random.randint(0,25)
		self.attMod = str('1.' + self.attMod)
		self.attMod = float(self.attMod)

class ChocolateBar(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Chocolate Bar'
		self.useCount = 4
		self.attMod = random.randint(0,40)
		self.attMod = str('2.' + self.attMod)
		self.attMod = float(self.attMod)

class NerdBomb(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Nerd Bomb'
		self.useCount = 1
		val1 = random.randint(3,5)
		val2 = random.randint(0,99)
		if val1 is 3 and val2 < 50:
			self.attMod = 3.5
		elif val1 is 5 and val2 > 0:
			self.attMod = 5.0
