import pygame, os

import World
import Image

from StaticObject import *
from MovableObject import *

import CONFIG

class WorldReader:

	AIR = (255,255,255) 
	GROUND = (34,177,76)
	
	GROUNDDEEP = (44,123,19)
	GROUNDDEEPLEFT = (33,90,14)
	GROUNDDEEPRIGHT= (53,146,22)
	
	GROUNDEDGELEFT = (13,155,95)
	GROUNDEDGERIGHT = (15,193,118)
	GROUNDEDGEBOTH = (14,175,106)
	
	WALL = (120,120,120)

	# World Reader returns an array of informations given by the map files
	# the return array has this format:
	# 
	#
	# [ <array of static objects>,
	#
	#	<array of movable objects>,
	#
	#	[<map width>, <map height>],
	#
	#	[<playerX_init>, <playerY_init>] ]
	#
	#
	# If world decides, that the player position is too close to the rim of
	# the map, it will define a new one.
	
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

				# delete alpha channel
				if(len(px) > 3):
					px = px[:3]

				posX = CONFIG.TILE_WIDTH * x
				posY = CONFIG.TILE_WIDTH * y

				if (px == self.AIR):
					staticObjects.append(AirObject([posX, posY]))
					
				elif (px == self.GROUND):
					staticObjects.append(GroundObject([posX, posY]))
				
				elif (px == self.GROUNDEDGELEFT):
					staticObjects.append(GroundELObject([posX, posY]))
				
				elif (px == self.GROUNDEDGERIGHT):
					staticObjects.append(GroundERObject([posX, posY]))
				
				elif (px == self.GROUNDEDGEBOTH):
					staticObjects.append(GroundEBObject([posX, posY]))
					
				elif (px == self.GROUNDDEEP):
					staticObjects.append(GroundDeepObject([posX, posY]))
				
				elif (px == self.GROUNDDEEPLEFT):
					staticObjects.append(GroundDeepLObject([posX, posY]))
				
				elif (px == self.GROUNDDEEPRIGHT):
					staticObjects.append(GroundDeepRObject([posX, posY]))
					
				elif (px == self.WALL):
					staticObjects.append(WallObject([posX, posY]))
					
				else:
					raise Exception("Tile type unknown: " + str(px))
				#endif
			#end for
		#end for

		# TODO insert moving objects
		# TODO initial player position
		
		initial_player_position = [0,0]

		return [staticObjects,
				movableObjects,
				staImg.size,
				initial_player_position]
		
		
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
					
					posX = CONFIG.TILE_WIDTH * i
					posY = CONFIG.TILE_WIDTH * j

					if (lines[i][j] == "0"):
						staticObjects.append(AirObject([posX, posY]))
					elif (lines[i][j] == "1"):
						staticObjects.append(GroundObject([posX, posY]))
					elif (lines[i][j] == "2"):
						staticObjects.append(WallObject([posX, posY]))
					else:
						raise Exception("Tile type unknown")
					j = j+1
				
			i = i+1

		# TODO insert moving objects

		return [staticObjects, movableObjects]
