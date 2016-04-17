import pygame, os

import CONFIG


class WorldView:

	images = {} 
	screen = None
	world = None
	pxwidth = None # window width
	pxheight = None # window height
	bgShiftV = None # vertical background image shift
	bgShiftH = None # horizontal background image shift

	def __init__(self, world):

		print("World View initialised")
		
		self.pxwidth  = CONFIG.VISIBLE_TILES_H*CONFIG.TILE_WIDTH
		self.pxheight = CONFIG.VISIBLE_TILES_V*CONFIG.TILE_HEIGHT
		
		self.size = self.pxwidth, self.pxheight
		
		self.bgShiftV = (self.pxheight - CONFIG.BG_IMG_HEIGHT) / 2
		self.bgShiftH = (self.pxwidth - CONFIG.BG_IMG_WIDTH) / 2
		
		self.world = world

		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
	

	def loadImages(self, pathlist):
		
		# debug msg
		print("world view loading images")

		for p in pathlist:
			img = pygame.image.load(pathlist[p]).convert_alpha()
			self.images.update({p:img})

		# debug msg
		print("amount images: " + str(len(self.images)))
				

	def show(self):

		
		playerPosition = self.world.player.position
		
		objs_in_range = self.world.objectsSurrounding(playerPosition)
		
		# debug msg
		print("Objects in range: " + str(len(objs_in_range)))
		
		# background
		self.screen.blit(self.images["Background"],(self.bgShiftH, self.bgShiftV))

		# player
		self.screen.blit(self.images[self.world.player.currentImg],
				pygame.Rect(self.pxwidth/2 - CONFIG.TILE_WIDTH / 2,
					playerPosition[1],
					CONFIG.TILE_WIDTH  * 2,
					CONFIG.TILE_HEIGHT * 2))
		
		for obj in objs_in_range:
			
			if (obj.visible):
				
				plotx = obj.position[0] - playerPosition[0] + self.pxwidth/2
				ploty = obj.position[1] 
				
				self.screen.blit(self.images[obj.currentImg], pygame.Rect(plotx, ploty, CONFIG.TILE_WIDTH,CONFIG.TILE_HEIGHT))

		pygame.display.flip()


	def setObjectImage (self,worldObject,image):
		worldObject.currentImg = self.images[image]
		
		
		
