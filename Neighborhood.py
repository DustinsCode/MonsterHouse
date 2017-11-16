from House import House

class Neighborhood():

	def __init__(self, game):
		x, y = 3, 3
		self.houseArray = [[House(game) for i in range(x)] for y in range(y)]
