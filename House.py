from Monster import *
from Oberver import Observer
from Observable import Observable


class House(Observer, Obervable):
"""
A house object
"""
    #TODO: find a better way to randomly fill with monsters
	def __init__(self, monsters, game):
		super().register(game)
		self.population = random.randint(0,10)
		self.monsters = []
		self.people = []
		for i in range(self.population):
			monsterList = [Zombie(), Werewolf(), Vampire(), Ghoul()]
			monsterIndex = random.randint(0,len(monsterList)-1)
			self.monsters.append(monsterList[monsterIndex])

	def update(self, *args):
		for monster in args:
			self.monsters.remove(monster)
			self.people.append(Person())
		update_observer(len(args))

	def getMonsters(self):
		return self.monsters
