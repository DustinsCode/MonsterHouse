from Observable import Observable
from House import *
from Weapon import *
import random

class Monster(Observable):
	"""
	Monsters that have infested the world.
	Player must turn them into Persons again.
	"""
	def __init__(self, House):
		"""
		Default constructor.
		"""
		super().__init__()
		super().register(House)
		self.type = ''
		self.health = 1

	def getType(self):
		"""
		returns monster's type
		"""
		return self.type

	def getHealth(self):
		"""
		returns monster's Health and checks if ded
		"""
		if self.health <= 0:
			super().update_observer(self)
			self.health = 0
		return self.health

class Person(Monster):
	"""
	Monster turns into this once their health is dropped to 0.
	Gives player health through the power of freindship.
	"""

	def __init__(self, House):
		super().__init__(House)
		self.type = "Person"
		self.health = 100

	def attack(self):
		"""
		Gives the player 3 health.
		"""
		return -3

	def attacked(self, dmg, weapon):
		return

class Zombie(Monster):
	"""
	Health between 50 and 100.  Attacks between 0 and 5.
	"""

	def __init__(self, House):
		super().__init__(House)
		self.type = "Zombie"
		self.health = random.randint(10,20)

	def attack(self):
		return random.randint(0,5)

	def attacked(self, dmg, weapon):
		if(weapon.getType() == "Sour Straw"):
			self.health -= dmg*2
		else:
			self.health -= dmg

		self.getHealth()

class Vampire(Monster):
	"""
	Health between 100 and 200. Attacks between 1 and 6.
	"""

	def __init__(self, House):
		super().__init__(House)
		self.type = "Vampire"
		self.health = random.randint(20,40)

	def attack(self):
		return random.randint(1,6)

	def attacked(self, dmg, weapon):
		if weapon.getType() == "Chocolate Bar":
			self.getHealth()
			return
		else:
			self.health = self.health - dmg
		self.getHealth()


class Ghoul(Monster):
	"""
	Health between 40 and 80.  Attacks between 5 and 10.
	"""

	def __init__(self, House):
		super().__init__(House)
		self.type = "Ghoul"
		self.health = random.randint(40,80)

	def attack(self):
		return random.randint(5,10)

	def attacked(self, dmg, weapon):
		if weapon.getType() == "Nerd Bomb":
			self.health -= dmg*5
		else:
			self.health -= dmg
		self.getHealth()

class Werewolf(Monster):
	"""
	Health of 60.  Attacks between 10 and 20.
	"""

	def __init__(self, House):
		super().__init__(House)
		self.type = "Werewolf"
		self.health = 60

	def attack(self):
		return random.randint(10,20)

	def attacked(self, dmg, weapon):
		if weapon.getType() == "Chocolate Bar" or weapon.getType() == "Sour Straw":
			self.getHealth()
		else:
			self.health -= dmg
		self.getHealth()
