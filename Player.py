import random
from Weapon import *

class Player():

	def __init__(self):
		self.hp = random.randint(100,125)
		self.attVal = random.randint(10,20)
		self.weapons = [HersheyKiss()]
		for x in range(9):
			possibleWeapons = [SourStraw(), ChocolateBar(), NerdBomb()]
			windex = random.randint(0,2)
			self.weapons.append(possibleWeapons[windex])

	def attack(Weapon):
		return self.attVal * Weapon.getAttMod()

	def getHp(self):
		return hp

	def getWeapons(self):
		return self.weapons
