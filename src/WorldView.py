import pygame, os

class WorldView:

	images = {} 
	size = width, heigth = 500,300
	screen = None
	world = None

	def __init__(self, world):
		print("World View initialised")
		self.world = world
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
	

	def loadImages(self, pathlist):
		for p in pathlist:
			img = pygame.image.load(pathlist[p]).convert()
			self.images.update({p:img})
				

	def show(self):

		playerPosition = self.world.player.position
		
		objs_in_range = self.world.objecsSurrounding(playerPositon)
		
		screen.fill((0,0,0))

		for obj in objs_in_range:
			
			if (obj.visible):
				
				plotx = obj.position[0] - playerPosition[0] + self.width/2
				ploty = obj.position[1] + self.heigh/2
				
				screen.blit(self.images[obj.img], pygame.Rect(plotx, ploty, 100,100))

		pygame.display.flip()


	def setObjectImage (self,worldObject,image):
		worldObject.currentImg = self.images[image]
		
		
		