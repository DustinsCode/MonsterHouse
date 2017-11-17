from Observable import Observable
from Weapon import *
import random


class Monster(Observable):

	def __init__(self, house):
		super().register(house)
		self.type = ''
		self.attack = 0
		self.health = 0

	def getType(self):
		return self.type


class Person(Monster):

	def __init__(self):
		super().__init__()
		self.type = "Person"
		self.attack = -1
		self.health = 100

	def attack(self):
		return self.attack

class Zombie(Monster):

	def __init__(self):
		super().__init__()
		self.type = "Zombie"
		self.health = random.randint(50,100)

	def attack(self):
		return random.randint(0,5)



class Vampire(Monster):

	def __init__(self):
		#super().__init__()
		self.type = "Vampire"
		self.health = random.randint(100,200)

	def attack(self):
		return random.randint(1,6)

class Ghoul(Monster):

	def __init__(self):
		#super().__init__()
		self.type = "Ghoul"
		self.health = random.randint(40,80)

	def attack(self):
		return random.randint(5,10)

class Werewolf(Monster):

	def __init__(self):
		#super().__init__()
		self.type = "Werewolf"
		self.health = 200

	def attack(self):
		return random.randint(10,20)
