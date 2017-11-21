import random
from Weapon import *
from Observable import *

class Player(Observable):
	"""
	Class that represents the Player of the game.
	Our protagonist, if you will.
	"""

	def __init__(self, game):
		"""
		Default constructor.
		"""
		super().__init__()
		super().register(game)
		self.hp = random.randint(100,125)
		self.attVal = random.randint(10,20)
		self.weapons = [HersheyKiss()]
		for x in range(9):
			possibleWeapons = [SourStraw(), ChocolateBar(), NerdBomb()]
			windex = random.randint(0,2)
			self.weapons.append(possibleWeapons[windex])

	def attack(self, Weapon):
		"""
		Returns the amount of damage done by the player.
		Mulitplies base attack by weapon's attack modifier.
		"""
		return self.attVal * Weapon.getAttMod()

	def updateWeapons(self, weapon):
		"""
		Removes weapon if useCount reaches 0.
		"""
		weapon.use()
		if weapon.getUseCount() == 0:
			self.weapons.remove(weapon)

	def attacked(self, dmg):
		"""
		Decrements HP by amount of damage given.
		"""
		self.hp -= dmg
		self.getHp()

	def getHp(self):
		"""
		Returns player's health value.
		"""
		if self.hp <= 0:
			super().update_observer()
		return self.hp

	def getWeapons(self):
		"""
		Returns list of player's current weapons.
		"""
		return self.weapons
