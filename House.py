from Monster import *
from Observer import *
from Observable import Observable


class House(Observer, Observable):
	"""
	A house object.  Populates with 0-6 monsters
	"""
	def __init__(self, game):
		super().__init__()
		super().register(game)
		self.population = random.randint(0,6)
		self.monsters = []
		self.people = []
		self.containsPlayer = False
		for i in range(self.population):
			monsterList = [Zombie(self), Werewolf(self), Vampire(self), Ghoul(self)]
			monsterIndex = random.randint(0,len(monsterList)-1)
			self.monsters.append(monsterList[monsterIndex])

	def playerMove(self):
		if self.containsPlayer:
			self.containsPlayer = False
		else:
			self.containsPlayer = True


	def update(self, *args):
		"""
		updates the observer and is updated by monsters
		"""
		for monster in args:
			self.monsters.remove(monster)
			self.people.append(Person())
		super().update_observer()

	def getMonsters(self):
		"""
		Returns list of monsters in the house.
		"""
		return self.monsters

	def getPeople(self):
		"""
		Returns list of Person objects in the house.
		"""
		return self.people
