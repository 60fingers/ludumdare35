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
		self.movables = worldobjects[0]
		self.statics = worldobjects[1]

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

		while (i < (self.levelheight * (x + self.surroundarea))):
			surroundings.append(self.movables[i])
			i+=1
		
		# add every movable object in range
		for m in self.movables:
			if (m.position[0] >= (x - self.surroundarea) and
					m.position[0] <= (x + self.surroundarea)):
				surroundings.append(m)
			
		return surroundings
		
	def nextStep(self,keys):
		
		if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			if(self.player.position[0] >= 0):
				self.player.position[0] -= self.player.maxSpeed
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.player.position[0] += self.player.maxSpeed
