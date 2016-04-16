import pygame, os

class WorldView:

	images = {} 
	size = width, heigth = 500,300
	screen = none

	def __init__(self):
		print("World View initialised")
		pygame.init()
		self.screen = pygame.display.set_mode(size)
	

	def loadImages(pathlist):
		for p in pathlist:
			img = pygame.image.load(pathlist[p]).convert()
			self.images.Update({p:img})
				

	def show(self, playerPosition):
		
		objs_in_range = world.objecsSurrounding(playerPositon)
		
		screen.fill((0,0,0))

		for obj in objs_in_range:
			
			if (obj.visible):
				
				plotx = obj.position[0] - playerPosition[0] + self.width/2
				ploty = obj.position[1] + self.heigh/2
				
				screen.blit(self.images[img], pygame.Rect(plotx, ploty, 128,128))

		pygame.display.flip()

