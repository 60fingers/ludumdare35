import pygame, os

import WorldView
import World

class MainControl:

	world = None
	view = None

	def __init__(self):
		self.world = World.World()
		self.view = WorldView.WorldView(self.world)

		self.view.loadImages(Auxiliaries.readImagePathList())

		self.running = true

	def main(self):

		while self.running:
			
			# check for quit event
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					sys.exit()

			# input for player control
			keys = pygame.key.get_pressed()

			world.nextStep(keys)
			view.show()
			time.sleep(0.01)

		#end while

		print("quit")
		sys.exit()
		
