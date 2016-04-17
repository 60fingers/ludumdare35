import pygame, os, datetime, random

from MovableObject import MovableObject

import CONFIG

class Player (MovableObject):
			
	currentKeys = "" # leerer String, wird durch passenden String ersetzt
	lastKeys = "" # siehe oben
	lastKeyTime = "" # siehe oben, TODO welches Zeitformat verwenden wir hier?	
	currentShape = 0 # Shapes 0=human, 1=gepart, 2=snake, 3=bird
	
			
	def __init__ (self, position):
		MovableObject.__init__(self,
			position,
			collision=True,
			imglist=["PlayerRunningLeft1", "PlayerRunningLeft2", "PlayerRunnungRight1", "PlayerRunnungRight2", "PlayerStandingLeft", "PlayerStandingRight"],
			animated=False,
			frameDuration = 10,
			currentImg = None,
			visible=True,
			maxSpeed=CONFIG.PLAYER_SPEED_HUMAN)
		self.lastShift = 0 # cooldown timer
	
	def nextStep(self, keys):
		
		# Shapeshift
		timeSinceLastShift = (pygame.time.get_ticks() - self.lastShift)/1000
		if(timeSinceLastShift >= 5):
		
			if(keys[pygame.K_SPACE]):
			
				currentShape=random.randint(0,3)
				print("Shift into shape " + str(currentShape))
				# Cooldown
				self.lastShift = pygame.time.get_ticks()
				
		MovableObject.nextStep(self)
		
		
		
		
		#if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			#self.position[0] += self.maxSpeed
		#if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			#self.position[0] -= self.maxSpeed
		#if(keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
			#self.position[1] -= self.maxSpeed
		#if(keys[pygame.K_DOWN] and not keys[pygame.K_UP]):
			#self.position[1] += self.maxSpeed
		
		

