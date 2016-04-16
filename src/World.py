import pygame, os
from Player import Player
from StaticObject import *
from MovableObject import *

from WorldReader import WorldReader


class World:

	player = None
	movables = []
	stativs = []

	# range for -> objectsSurrounding
	surroundarea = 10
	
	# read maps and mob positions
	def __init__(self):
		
		# debug msg
		print("reading maps")
		
		worldobjects = WorldReader().readImage("../maps/world1stat.png","../maps/world1mov.png")
		self.statics = worldobjects[0]
		self.movables = worldobjects[1]

		#TODO: test wich values to take / read height from map
		self.levelheight = 10

		self.player = Player([0,0])	# TODO echte Spielerposition verwenden!
	

	# find stativ objects and mobs within defined range around a position
	def objectsSurrounding(self, position):

		# list of map objects within range
		surroundings = []

		x = position[0]

		# add every static object in range
		i = (self.levelheight * (x - self.surroundarea))

		# no indices <0 would result in searching from the other end (eg. list[-3])
		# -> left edge of the map
		if(i<0):
			i = 0

		while (i < (self.levelheight * (x + self.surroundarea))):
			print(position)
			surroundings.append(self.statics[i])
			i+=1

			# right edge of the map
			if(i >= len(self.statics)):
				break

		
		# add every movable object in range
		for m in self.movables:
			if (m.position[0] >= (x - self.surroundarea) and
					m.position[0] <= (x + self.surroundarea)):
				surroundings.append(m)
			
		return surroundings
		
	def nextStep(self,keys):
		
		if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			if(self.player.position[0] >= self.player.maxSpeed):
				self.player.position[0] -= self.player.maxSpeed
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.player.position[0] += self.player.maxSpeed
