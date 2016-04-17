import pygame, os
from Player import Player
from StaticObject import *
from MovableObject import *

from WorldReader import WorldReader

import CONFIG

class World:

	player = None
	movables = []
	statics = []

	# read maps and mob positions
	def __init__(self):
		
		# debug msg
		print("reading maps")
		
		worldobjects = WorldReader().readImage("../maps/world1stat.png",
			"../maps/world1mov.png")
		self.statics = worldobjects[0]
		self.movables = worldobjects[1]

		#TODO: test wich values to take / read height from map
		self.levelheight = 10

		self.player = Player([0,0],self)	# TODO echte Spielerposition verwenden!
	

	# find stativ objects and mobs within defined range around a position
	def objectsSurrounding(self, position, radius):

		# list of map objects within range
		surroundings = []

		x = position[0]/CONFIG.TILE_WIDTH

		# add every static object in range
		#------------- BEGIN ----------------

		i = (self.levelheight * (x - radius))

		# no indices <0 would result in searching from the other end (eg. list[-3])
		# -> left edge of the map
		if(i<0):
			i = 0

		while (i < self.levelheight * (x + radius)):

			surroundings.append(self.statics[i])
			i+=1

			# right edge of the map
			if(i >= len(self.statics)):
				break

		#------------- END -----------------
		

		# add every movable object in range
		#------------ BEGIN ----------------

		for m in self.movables:
			
			mx = m.position[0] / CONFIG.TILE_WIDTH

			if (mx >= (x - radius) and
					mx <= (x + radius)):
				surroundings.append(m)
			
		#------------- END -----------------

		return surroundings
		


	def nextStep(self,keys):
		

		for s in self.statics:
			s.nextStep()

		for m in self.movables:
			m.nextStep()
			m.correctCollision(self)
			

		self.player.nextStep(keys)
		
		#self.player.correctCollision(self)
		
		# TODO HACK Testzwecke:
		if(self.player.position[0] < 0):
			self.player.position[0] = 0
		if(self.player.position[0] >= (len(self.statics) * CONFIG.TILE_WIDTH)):
			self.player.position[0] = (len(self.statics)-1) * CONFIG.TILE_WIDTH
		if(self.player.position[1] < 0):
			self.player.position[1] = 0
		if(self.player.position[1] >= (self.levelheight * CONFIG.TILE_HEIGHT)):
			self.player.position[1] = (self.levelheight * CONFIG.TILE_HEIGHT)-1

