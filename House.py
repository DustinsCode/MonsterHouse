from Monster import *
from Oberver import Observer
from Observable import Observable


class House(Observer, Obervable):
"""
A house object
"""
    def __init__(self, monsters, game):
        super().register(game)
        self.population = random.randint(0,10)
        self.monsters = []
        self.people = []
        for i in range(self.population):
            monsterIndex = random.randint(0,len(monsters)-1)
            personChance = random.randint(1,10)
            self.monsters.append(monsters[monsterIndex])

    def update(self, *args):
        for monster in args:
            self.monsters.remove(monster)
            self.people.append(Person())
        update_observer(len(args))
