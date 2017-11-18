from House import House

class Neighborhood():
	"""
	A 2d array representing the game's map.
	"""

	def __init__(self, game):
		x, y = 3, 3
		self.houseArray = [[House(game) for i in range(x)] for y in range(y)]
