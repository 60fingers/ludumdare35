import pygame, os

class WorldView:

	images = {} 
	screen = None
	world = None

	def __init__(self, world):

		print("World View initialised")
		self.size = self.width, self.heigth = 1280,900
		self.world = world

		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
	

	def loadImages(self, pathlist):
		
		# debug msg
		print("world view loading images")

		for p in pathlist:
			img = pygame.image.load(pathlist[p]).convert()
			self.images.update({p:img})

		# debug msg
		print("amount images: " + str(len(self.images)))
				

	def show(self):

		
		playerPosition = self.world.player.position
		
		objs_in_range = self.world.objectsSurrounding(playerPosition)
		
		self.screen.blit(self.images["Background"],(0,0))

		# debug msg
		#print("Objects in range: " + str(len(objs_in_range)))
		
		for obj in objs_in_range:
			
			if (obj.visible):
				
				plotx = obj.position[0] - playerPosition[0] + self.width/2
				ploty = obj.position[1] 
				
				self.screen.blit(self.images[obj.currentImg], pygame.Rect(plotx, ploty, 100,100))

		pygame.display.flip()


	def setObjectImage (self,worldObject,image):
		worldObject.currentImg = self.images[image]
		
		
		
