import random

class Player():

	def __init__(self):
		self.hp = random.randint(100,125)
		self.attVal = random.randint(10,20)
		self.weapons = []
