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
		self.world.loadSounds(Auxiliaries.readSoundPathList())
		self.running = True
		
		self.debugToggle = 0

	def main(self):

		self.world.sounds["Start"].play()
		
		while self.running:
			
			# check for quit event
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					sys.exit()

			# input for player control
			keys = pygame.key.get_pressed()
			
			## DEBUG FUNC ##
			if(keys[pygame.K_c] and (pygame.time.get_ticks() - self.debugToggle > 100)):
				CONFIG.DEBUGMODE = not CONFIG.DEBUGMODE
				self.debugToggle = pygame.time.get_ticks()
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
		
