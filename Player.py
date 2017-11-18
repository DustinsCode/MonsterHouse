import random
from Weapon import *

class Player():
	"""
	Class that represents the Player of the game.
	Our protagonist, if you will.
	"""

	def __init__(self):
		"""
		Default constructor.
		"""
		self.hp = random.randint(100,125)
		self.attVal = random.randint(10,20)
		self.weapons = [HersheyKiss()]
		for x in range(9):
			possibleWeapons = [SourStraw(), ChocolateBar(), NerdBomb()]
			windex = random.randint(0,2)
			self.weapons.append(possibleWeapons[windex])

	def attack(Weapon):
		"""
		Returns the amount of damage done by the player.
		Mulitplies base attack by weapon's attack modifier.
		"""
		return self.attVal * Weapon.getAttMod()

	def getHp(self):
		"""
		Returns player's health value.
		"""
		return self.hp

	def getWeapons(self):
		"""
		Returns list of player's current weapons.
		"""
		return self.weapons
