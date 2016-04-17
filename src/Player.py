import pygame, os, datetime, random

from MovableObject import MovableObject
from PlayerModes import PlayerHuman, PlayerGepard, PlayerSnake, PlayerBird

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
		self.lastShift = 0 # cooldown timer
		self.currentShape = 0 # Shapes 0=human, 1=gepard, 2=snake, 3=bird
		self.currentPlayermode = PlayerHuman(self)
		self.jumpSpeed = CONFIG.PLAYER_JUMP_SPEED_HUMAN
		self.facingForward = True
		self.canHover = False
	
	def nextStep(self, keys):
		
		# Shapeshift
		timeSinceLastShift = (pygame.time.get_ticks() - self.lastShift)/1000
		if(timeSinceLastShift >= CONFIG.PLAYER_SHAPESHIFT_COOLDOWN):
		
			if(keys[pygame.K_SPACE]):
			
				self.currentShape=random.randint(0,3)
				if(self.currentShape == 0):
					self.currentPlayermode = PlayerHuman(self)
				elif(self.currentShape == 1):
					self.currentPlayermode = PlayerGepard(self)
				elif(self.currentShape == 2):
					self.currentPlayermode = PlayerSnake(self)
				elif(self.currentShape == 3):
					self.currentPlayermode = PlayerBird(self)
						
				print("Shift into shape " + str(self.currentShape))
				# Cooldown
				self.lastShift = pygame.time.get_ticks()
			
		self.currentPlayermode.nextStep(keys)
		MovableObject.nextStep(self)
		
		
		