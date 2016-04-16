import pygame, os

import World
import Image

from StaticObject import *
from MovableObject import *

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
					staticObjects.append(AirObject([100*x, 100*y]))
				elif (px == self.GROUND):
					staticObjects.append(GroundObject([100*x, 100*y]))
				elif (px == self.WALL):
					staticObjects.append(WallObject([100*x, 100*y]))
				else:
					raise Exception("Tile type unknown")
				#endif
			#end for
		#end for

		# TODO insert moving objects

		return [staticObjects, movableObjects]
