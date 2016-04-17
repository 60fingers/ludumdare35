import pygame, os, time, sys, sys

import WorldView
import World
import Auxiliaries

import CONFIG

class MainControl:


	world = None
	view = None

	def __init__(self):
		self.world = World.World()
		self.view = WorldView.WorldView(self.world)

		self.view.loadImages(Auxiliaries.readImagePathList())

		self.running = True

	def main(self):

		while self.running:
			
			# check for quit event
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					sys.exit()

			# input for player control
			keys = pygame.key.get_pressed()
			
			## DEBUG FUNC ##
			if(keys[pygame.K_ESCAPE]):
				sys.exit()
			if(keys[pygame.K_BACKSPACE]):
				self.world.player.position[1] = 0
			## END DEBUG FUNC ##
				
			self.world.nextStep(keys)
			self.view.show()
			time.sleep(1/float(CONFIG.FPS))
			

		#end while

		print("quit")
		sys.exit()
		
