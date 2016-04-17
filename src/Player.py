import pygame, os, datetime 

from MovableObject import MovableObject

import CONFIG

class Player (MovableObject):
			
	currentKeys = "" # leerer String, wird durch passenden String ersetzt
	lastKeys = "" # siehe oben
	lastKeyTime = "" # siehe oben, TODO welches Zeitformat verwenden wir hier?	

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
	
	def nextStep(self, keys):
		
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.position[0] += self.maxSpeed
		if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			self.position[0] -= self.maxSpeed
		if(keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
			self.position[1] -= self.maxSpeed
		if(keys[pygame.K_DOWN] and not keys[pygame.K_UP]):
			self.position[1] += self.maxSpeed
		
		self.nextFrame()

