#!/usr/bin/python3

#from Monster import *
#from House import *
#from Weapon import *
from Player import Player
from Neighborhood import Neighborhood
from Observer import Observer

class Game(Observer):

	def __init__(self):
		self.message = ""
		self.hood = Neighborhood(self)
		self.p = Player()

	def main(self):

		Game.printMessage("Welcome to the spooky neighborhood.")
		Game.message("Please save your friends, they're all monsters now.")


	def printMessage():
		print()

g = Game()
g.main()
