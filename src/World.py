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
		
		# map information: list: [static object list, mob list, map size]
		mapInformations = WorldReader().readImage("../maps/world1stat.png",
			"../maps/world1mov.png")
		self.statics = mapInformations[0]
		self.movables = mapInformations[1]

		# pixelheight of the map
		self.levelheight = mapInformations[2][1]

		# extreme x coordinates, so that the player wont see the end of the world
		self.legalX_min = CONFIG.TILE_WIDTH * (CONFIG.VISIBLE_TILES_H/2 +1)
		self.legalX_max = (CONFIG.TILE_WIDTH * mapInformations[2][0] ) - self.legalX_min

		
		# initial position -> set to minimum if the one set by the map file isn't a
		# legal one
		if ( mapInformations[3][0] < self.legalX_min or
				mapInformations[3][0] > self.legalX_max):

			self.player = Player([self.legalX_min,0],self)
	

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
		

	# not column by column, but row by row
	def objSurr_H_static(self, position, radius):
		

		objs = []

		# x index of the tile
		xi = position[0] / CONFIG.TILE_WIDTH

		# index of the first tile
		ai = self.levelheight * (xi-radius)

		i = 0
		# whole block: "length * height"
		while (i < self.levelheight * 2 * radius):
			
			li = ( (i * self.levelheight) %  # jump in levelheight-steps
					(2 * radius * self.levelheight ) + # modulo "block width" to not get too far
					i/(2*radius) + # line and line and line
					ai ) # first index
			
			if (li >= len(self.statics) or li < 0):
				i+=1
				continue

			objs.append(self.statics[li])

			i+=1

		return objs

		

	def nextStep(self,keys):
		

		for s in self.statics:
			s.nextStep()

		for m in self.movables:
			m.nextStep()
			m.correctCollision(self)
			

		self.player.nextStep(keys)
		
		
		# dont leave the world
		if(self.player.position[0] < self.legalX_min):
			self.player.position[0] = self.legalX_min
		if(self.player.position[0] >= self.legalX_max):
			self.player.position[0] = self.legalX_max
		if(self.player.position[1] < 0):
			self.player.position[1] = 0
		if(self.player.position[1] >= (self.levelheight * CONFIG.TILE_HEIGHT)):
			self.player.position[1] = (self.levelheight * CONFIG.TILE_HEIGHT)-1

