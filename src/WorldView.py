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
		
		# visible screen in pixels
		self.pxwidth  = CONFIG.VISIBLE_TILES_H*CONFIG.TILE_WIDTH
		self.pxheight = CONFIG.VISIBLE_TILES_V*CONFIG.TILE_HEIGHT
		
		# screen size for pygame interface
		self.size = self.pxwidth, self.pxheight
		
		# centering background without scaling it
		self.bgShiftV = (self.pxheight - CONFIG.BG_IMG_HEIGHT) / 2
		self.bgShiftH = (self.pxwidth - CONFIG.BG_IMG_WIDTH) / 2
		

		self.world = world

		# pygame initialisation
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
	

	# is run once, before the game starts
	def loadImages(self, pathlist):
		
		print("WORLDVIEW: world view loading images")

		# load all the images and add it to the View's image dictionary
		for p in pathlist:
			img = pygame.image.load(pathlist[p]).convert_alpha()
			self.images.update({p:img})

		print("WORLDVIEW: amount images: " + str(len(self.images)))
				

	# main routine of world view, generates visible frame
	def show(self):

		
		# player position measured in pixels
		playerPosition = self.world.player.position
		
		# array of all objects within visible range
		objs_in_range = self.world.objectsSurrounding(playerPosition, CONFIG.RANGE_OF_VIEW)
		
		# show background, centered
		self.screen.blit(self.images["Background"],(self.bgShiftH, self.bgShiftV))


		# show player in the middle of the screen
		self.screen.blit(self.images[self.world.player.currentImg],
				pygame.Rect(self.pxwidth/2 - ( self.world.player.hsize * CONFIG.TILE_WIDTH) / 2,
					playerPosition[1],
					CONFIG.TILE_WIDTH, # deleted factor 2, i think it might be a bug, Till 17.04., 23:11
					CONFIG.TILE_HEIGHT * 2))

		

		for obj in objs_in_range:
			
			# show only objects with visible flag
			if (obj.visible):
				
				# show everything relatively to player, player is always in center
				plotx = obj.position[0] - playerPosition[0] + self.pxwidth/2 - CONFIG.TILE_WIDTH/2
				ploty = obj.position[1] 
				
				# show corresponding image from imagelist
				self.screen.blit(self.images[obj.currentImg], pygame.Rect(plotx, ploty, CONFIG.TILE_WIDTH,CONFIG.TILE_HEIGHT))

		pygame.display.flip()


	def setObjectImage (self,worldObject,image):
		worldObject.currentImg = self.images[image]
		
		
		
