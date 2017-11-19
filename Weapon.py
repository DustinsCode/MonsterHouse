import random

class Weapon():
	"""
	Weapons for the player to use
	"""

	def __init__(self):
		"""
		Default constructor.
		"""
		self.type = ''
		self.attMod = 1
		self.useCount = 0

	def getAttMod(self):
		"""
		Return's the weapon's attack modifier.
		"""
		return self.attMod

	def getType(self):
		"""
		Returns the weapon's type.
		"""
		return self.type

	def getUseCount(self):
		"""
		Returns the number of times an item can be used.
		"""
		return self.useCount

	def use(self):
		"""
		Decrements the use count of the weapon.
		"""
		self.useCount -= 1

class HersheyKiss(Weapon):
	"""
	Basic attack. Player has unlimited attacks with these.
	"""

	def __init__(self):
		super().__init__()
		self.type = 'Hershey Kiss'
		self.useCount = -1
		self.attMod = 1

class SourStraw(Weapon):
	"""
	Attack mod of 1-1.75.  Can be used twice.
	"""
	def __init__(self):
		super().__init__()
		self.type = 'Sour Straw'
		self.useCount = 2
		self.attMod = random.randint(100,175) / 100

class ChocolateBar(Weapon):
	"""
	Attack Mod of 1-1.4.  Can be used 4 times.
	"""

	def __init__(self):
		super().__init__()
		self.type = 'Chocolate Bar'
		self.useCount = 4
		self.attMod = random.randint(100,140) / 100

class NerdBomb(Weapon):
	"""
	Attack Mod of 3.5-5.0.  Can only be used 1 time.
	"""

	def __init__(self):
		super().__init__()
		self.type = 'Nerd Bomb'
		self.useCount = 1
		val1 = random.randint(350,500)/100
