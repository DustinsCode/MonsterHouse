import random

class Weapon():
	"""
	Weapons for the player to use
	"""

	def __init__(self):
		self.attMod = 1
		self.useCount = 0

	def getAttMod():
		return self.attMod


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
		self.useCount = 2
		self.attMod = random.randint(100,175) / 100

class ChocolateBar(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Chocolate Bar'
		self.useCount = 4
		self.attMod = random.randint(100,140) / 100

class NerdBomb(Weapon):

	def __init__(self):
		super().__init__()
		self.type = 'Nerd Bomb'
		self.useCount = 1
		val1 = random.randint(350,500)/100
