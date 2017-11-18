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
		self.attack = 0
		self.health = 0

	def getType(self):
		return self.type


class Person(Monster):
	"""
	Monster turns into this once their health is dropped to 0.
	Gives player health through the power of freindship.
	"""

	def __init__(self):
		super().__init__()
		self.type = "Person"
		self.attack = -1
		self.health = 100

	def attack(self):
		return self.attack

class Zombie(Monster):
	"""
	Health between 50 and 100.  Attacks between 0 and 5.
	"""

	def __init__(self, House):
		super().__init__(House)
		self.type = "Zombie"
		self.health = random.randint(50,100)

	def attack(self):
		return random.randint(0,5)



class Vampire(Monster):
	"""
	Health between 100 and 200. Attacks between 1 and 6.
	"""

	def __init__(self, House):
		#super().__init__()
		self.type = "Vampire"
		self.health = random.randint(100,200)

	def attack(self):
		return random.randint(1,6)

class Ghoul(Monster):
	"""
	Health between 40 and 80.  Attacks between 5 and 10.
	"""

	def __init__(self, House):
		#super().__init__()
		self.type = "Ghoul"
		self.health = random.randint(40,80)

	def attack(self):
		return random.randint(5,10)

class Werewolf(Monster):
	"""
	Health of 200.  Attacks between 10 and 20.
	"""

	def __init__(self, House):
		#super().__init__()
		self.type = "Werewolf"
		self.health = 200

	def attack(self):
		return random.randint(10,20)
