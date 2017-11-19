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

	Note:	I edited some of the provided values to balance the Game
			and make it winnable.

	@author Dustin Thurston
	"""

	def __init__(self):
		self.message = ""
		self.hood = Neighborhood(self)
		self.x = 1
		self.y = 1
		self.currHouse = self.hood.houseArray[self.x][self.y]
		self.currHouse.playerMove()
		self.p = Player()
		self.win = False
		self.commands = ["exit", "attack <weapon>", "move <north, easy, south, or west>", "inventory", "help", "look"]


	def main(self):
		"""
		Sets the initial welcome message and waits for user commands
		until the game winning conditions are met.
		"""
		self.message = ("\nWelcome to the spooky neighborhood.\n"
						"All of your friends have turned to monsters!\n"
						"Please help them!\n")
		self.printMessage()
		self.look()


		while(self.win == False):
			command = ''
			while(command == ''):
				command = input('> ')
				command = command.strip()
				command = command.lower()
			if self.parseCommand(command) == "exit":
				return


	def printMessage(self):
		"""
		Prints the game's current message.
		"""
		print(self.message)

	def parseCommand(self,command):
		"""
		Takes in a command given by the user and
		acts accordingly
		"""
		if(command == "inv" or command == "inventory"):
			self.getWeapons()
		elif(command == "exit" or command == "quit"):
			return "exit"
		elif(command == "help"):
			self.help()
		elif(command == "look"):
			self.look()
		elif("attack" in command):
			self.attack(command)
		else:
			self.message = "That is not a command."
			self.printMessage()

	def attack(self, command):
		cmdList = command.split(' ')
		if len(cmdList) > 3:
			self.message = "You must attack with one weapon at a time."
			self.printMessage()
		else:
			weapon = ''
			for x in cmdList[1:]:
				#Finds the weapon to be used
				weapon += x.lower()
			for y in self.p.getWeapons():
				if(weapon in y.getType().lower().strip()):
					weapon = y
					break
				weapon = ''

			if weapon == '':
				#if the weapon entered was invalid
				self.message = "That is not a weapon you possess."
				self.printMessage()
				return

			for monster in self.currHouse.getMonsters():
				#Attacks each monster in the house
				dmg = self.p.attack(weapon)
				monster.attacked(dmg, weapon)
				self.message = "Attacked " + monster.getType() + " for " + str(dmg) + " damage!"
				self.printMessage()
				monster.getHealth()
			self.p.updateWeapons(weapon)
			for person in self.currHouse.getPeople():
				self.p.attacked(person.attack())

		self.look()

	def look(self):
		self.message = ""
		self.message += "You are in a house with: \n"
		if len(self.currHouse.getMonsters()) == 0:
			self.message += "No monsters\n"
		else:
			for m in self.currHouse.getMonsters():
				self.message += m.getType() + "\n"
		if len(self.currHouse.getPeople()) == 0:
			self.message += "and no people."
		else:
			self.message += "and " + str(len(self.currHouse.getPeople())) + " people.\n"
		self.printMessage()


	def help(self):
		"""
		Prints a list of available commands to the player.
		"""
		temp = self.message
		self.message = "Here's a list of commands: \n"
		for s in self.commands:
			self.message += s + '\n'
		self.printMessage()
		self.message = temp

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
