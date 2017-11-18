#!/usr/bin/python3

#from Monster import *
#from House import *
from Weapon import *
from Player import Player
from Neighborhood import Neighborhood
from Observer import Observer

class Game(Observer):
	"""
	The Main class that runs and tracks the progress
	of the game.
	"""

	def __init__(self):
		self.message = ""
		self.hood = Neighborhood(self)
		self.p = Player()
		self.win = False

	def main(self):
		"""
		Sets the initial welcome message and waits for user commands
		until the game winning conditions are met.
		"""
		self.message = ("\nWelcome to the spooky neighborhood.\n"
						"All of your friends have turned to monsters!\n"
						"Please help them!\n")
		self.printMessage()

		while(self.win == False):
			command = ''
			while(command == ''):
				command = input('> ')
				command = command.strip()
			self.parseCommand(command)


	def printMessage(self):
		"""
		Prints the game's current message.
		"""
		print(self.message)

	def parseCommand(self,command):
		pass

	def getWeapons(self):
		"""
		Prints out a list of Player's current weapons.
		"""
		weapons = self.p.getWeapons()
		self.message = 'HersheyKiss xinfinity\n'
		nerdCount = 0
		strawCount = 0
		barCount = 0

		for w in weapons:
			wtype = w.getType()
			#print(wtype)
			if wtype == 'Nerd Bomb':
				nerdCount += 1
			elif wtype == 'Chocolate Bar':
				barCount += 1
			elif wtype == 'Sour Straw':
				strawCount += 1

		self.message = self.message + 'Sour Straw x' + str(strawCount) + '\n'
		self.message = self.message + 'ChocolateBar x'+ str(barCount) + '\n'
		self.message = self.message + 'Nerd Bomb x'+ str(nerdCount) + '\n'

		self.printMessage()


g = Game()
g.main()
