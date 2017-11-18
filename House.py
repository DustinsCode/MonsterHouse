from Monster import *
from Observer import *
from Observable import Observable


class House(Observer, Observable):
	"""
	A house object
	"""
    #TODO: find a better way to randomly fill with monsters
	def __init__(self, game):
		super().__init__()
		super().register(game)
		self.population = random.randint(0,10)
		self.monsters = []
		self.people = []
		for i in range(self.population):
			monsterList = [Zombie(), Werewolf(), Vampire(), Ghoul()]
			monsterIndex = random.randint(0,len(monsterList)-1)
			self.monsters.append(monsterList[monsterIndex])

	def update(self, *args):
		"""
		updates the observer and is updated by monsters
		"""
		for monster in args:
			self.monsters.remove(monster)
			self.people.append(Person())
		super().update_observer(len(args))

	def getMonsters(self):
		"""
		Returns list of monsters in the house.
		"""
		return self.monsters
