from Observable import Observable


class Monster(Observable):

	def __init__(self, house):
		super().register(house)


class Person():

	def __init__(self):
	self.type = "Person"

class Zombie():

	def __init__(self):
	self.type = "Zombie"

class Vampire():

	def __ init__(self):
	self.type = "Vampire"

class Ghoul():

	def __init__(self):
	self.type = "Ghoul"

class Werewolf():

	def __init__(self):
	self.type = "Werewolf"
