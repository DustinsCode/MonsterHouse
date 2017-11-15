from Observable import Observable


class Monster(Observable):

	def __init__(self, house):
		super().register(house)


class Person(Monster):

	def __init__(self):
		super().__init__()
		self.type = "Person"

class Zombie(Monster):

	def __init__(self):
		super().__init__()
		self.type = "Zombie"

class Vampire(Monster):

	def __init__(self):
		super().__init__()
		self.type = "Vampire"

class Ghoul(Monster):

	def __init__(self):
		super().__init__()
		self.type = "Ghoul"

class Werewolf(Monster):

	def __init__(self):
		super().__init__()
		self.type = "Werewolf"
