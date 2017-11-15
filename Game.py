#!/usr/bin/python3

#from Monster import *
#from House import *
#from Weapon import *
from Player import Player
from Neighborhood import Neighborhood
from Observer import Observer

class Game(Observer):

	def main(self):

		hood = Neighborhood(self)
		p = Player()

		Game.message("Welcome to the spooky neighborhood.")
		Game.message("Please save your friends, they're all monsters now.\n\n")

		#while(True):


	def message(m):
		print(m,'\n')

g = Game()
g.main()
