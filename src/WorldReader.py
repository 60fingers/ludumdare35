import pygame, os

import World
import Image

from StaticObject import *
from MovableObject import *

import CONFIG

class WorldReader:

	AIR = (255,255,255) 
	GROUND = (34,177,76)
	WALL = (120,120,120)
	
	def __init__(self):
		print("world reader in action")
	
	def readImage(self, pathStatic, pathMovable):
		
		staticObjects = []
		movableObjects = []

		staImg = Image.open(pathStatic)
		movImg = Image.open(pathMovable)

		if(staImg.size[0] != movImg.size[0]
			or staImg.size[1] != movImg.size[1]):
			raise Exception("'statics' and 'moving' maps have different sizes")


		pxmapStat = staImg.load()
		pxmapMove = movImg.load()

		for x in range(staImg.size[0]):
			for y in range(movImg.size[1]):
				
				px = pxmapStat[x,y]

				if (px == self.AIR):
					staticObjects.append(AirObject([CONFIG.TILE_WIDTH*x, CONFIG.TILE_HEIGHT*y]))
				elif (px == self.GROUND):
					staticObjects.append(GroundObject([CONFIG.TILE_WIDTH*x, CONFIG.TILE_HEIGHT*y]))
				elif (px == self.WALL):
					staticObjects.append(WallObject([CONFIG.TILE_WIDTH*x, CONFIG.TILE_HEIGHT*y]))
				else:
					raise Exception("Tile type unknown")
				#endif
			#end for
		#end for

		# TODO insert moving objects

		return [staticObjects, movableObjects]
		
		
	def readFile(self, pathFile):
		
		staticObjects = []
		movableObjects = []
		
		file = open(pathStatic,"r")
		lines = file.readlines()
		file.close()
		
		# iterating over all lines
		i = 0
		while (i < len(lines)):
			if(not lines[i]=="\n"):
				# iterating over every char in one string
				j = 0
				while (j < (len(lines[i])-1)):
					if (lines[i][j] == "0"):
						staticObjects.append(AirObject([CONFIG.TILE_WIDTH*i, CONFIG.TILE_HEIGHT*j]))
					elif (lines[i][j] == "1"):
						staticObjects.append(GroundObject([CONFIG.TILE_WIDTH*x, CONFIG.TILE_HEIGHT*y]))
					elif (lines[i][j] == "2"):
						staticObjects.append(WallObject([CONFIG.TILE_WIDTH*x, CONFIG.TILE_HEIGHT*y]))
					else:
						raise Exception("Tile type unknown")
					j = j+1
				
			i = i+1

		# TODO insert moving objects

		return [staticObjects, movableObjects]
