#!/usr/bin/env python3

#from Monster import *
#from House import *
#from Weapon import *
from Player import Player
from Neighborhood import Neighborhood
from Observer import observer

class Game(Observer):

	def main(self):

		hood = Neighborhood()
		p = Player()

		message("Welcome to the spooky neighborhood.")
		message("Please save your friends, they're all monsters now.\n\n")

		#while(True):


	def message(m):
		print(m,'\n')
