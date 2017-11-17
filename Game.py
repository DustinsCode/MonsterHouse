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
		self.message = ("\nWelcome to the spooky neighborhood.\n"
						"All of your friends have turned to monsters!\n"
						"Please help them!\n")
		self.printMessage()

		

	def printMessage(self):
		print(self.message)

g = Game()
g.main()
