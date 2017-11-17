#!/usr/bin/python3

#from Monster import *
#from House import *
from Weapon import *
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
		self.getWeapons()


	def printMessage(self):
		print(self.message)

	def getWeapons(self):
		weapons = self.p.getWeapons()
		self.message = 'HersheyKiss xinfinity\n'
		nerdCount = 0
		strawCount = 0
		barCount = 0

		for w in weapons:
			wtype = w.getType()
			if wtype is 'Nerd Bomb':
				nerdCount += 1
			elif wtype is 'Chocolate Bar':
				barCount += 1
			elif wtype is 'Sour Straw':
				strawCount += 1

		self.message = self.message + 'Sour Straw x' + str(strawCount) + '\n'
		self.message = self.message + 'ChocolateBar x'+ str(barCount) + '\n'
		self.message = self.message + 'Nerd Bomb x'+ str(nerdCount) + '\n'

		self.printMessage()


g = Game()
g.main()
