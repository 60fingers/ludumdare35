import pygame, os

import HUD

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

		# ui hud
		self.hud = HUD.HUD(self)
	

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
		if (not CONFIG.DEBUGMODE):
		
			self.screen.blit(self.images[self.world.player.currentImg],
					(self.pxwidth/2 - ( self.world.player.hsize * CONFIG.TILE_WIDTH) / 2,
					playerPosition[1]))
		
		else:
			player = self.world.player
			drawrect = pygame.Rect(self.pxwidth/2 - ( self.world.player.hsize * CONFIG.TILE_WIDTH) / 2,	playerPosition[1],	player.rect.width, player.rect.height) 
			pygame.draw.rect(self.screen, (100,100,255), drawrect )
		# end if DEBUG
		
		# show morph image
		if (pygame.time.get_ticks()- self.world.player.lastShift < 300):

			curMorph = pygame.transform.scale(self.images["Morph"],
					(int(CONFIG.TILE_WIDTH * self.world.player.hsize * 1.3),
					 int(CONFIG.TILE_WIDTH * self.world.player.vsize * 1.3)))
	
			self.screen.blit(curMorph,
					(self.pxwidth/2 - ( self.world.player.hsize * CONFIG.TILE_WIDTH * 1.3) / 2,
					playerPosition[1] - CONFIG.TILE_HEIGHT * 0.3))

		# end show morph

		

		for obj in objs_in_range:
			
			# show only objects with visible flag
			if (obj.visible):
				
				# show everything relatively to player, player is always in center
				plotx = (obj.position[0] - playerPosition[0] + 
						self.pxwidth/2 - CONFIG.TILE_WIDTH/2)
				ploty = obj.position[1] 
				
				# show objects
				if (not CONFIG.DEBUGMODE):
					# show corresponding image from imagelist
					self.screen.blit(self.images[obj.currentImg],
							pygame.Rect(plotx, ploty,
									CONFIG.TILE_WIDTH, CONFIG.TILE_HEIGHT))
				
				else:
					drawrect = pygame.Rect(plotx, ploty, obj.rect.width, obj.rect.height,)
					pygame.draw.rect(self.screen, (255,100,100), drawrect )
				# end if DEBUG
				
			# end if
		# end for

		self.hud.show()

		pygame.display.flip()


	def setObjectImage (self,worldObject,image):
		worldObject.currentImg = self.images[image]
		
		
		
