import pygame, os, random

from MovableObject import MovableObject
from PlayerModes import PlayerHuman, PlayerGepard, PlayerSnake, PlayerBird

import CONFIG

class Player (MovableObject):
			
			
	def __init__ (self, position, world):
		MovableObject.__init__(self,
			position,
			collision=True,
			world = world,
			imglist=["PlayerStandingLeft"],
			animated=True,
			frameDuration = 5,
			currentImg = None,
			visible=True,
			maxSpeed=CONFIG.PLAYER_SPEED_HUMAN)
			
		self.vsize = 1
		self.hsize = 2
		self.canHover = False
			
		self.lastShift = -1 # cooldown timer
		self.currentShape = 0 # Shapes 0=human, 1=gepard, 2=snake, 3=bird
		self.currentPlayermode = PlayerHuman(self)
		self.jumpSpeed = CONFIG.PLAYER_JUMP_SPEED_HUMAN
		self.facingForward = True
		self.lastTickVelY = 0
		
		self.currentAction = "sr" # possible: jr, jl, rl, rr, sr, sl
		
		
	
	def nextStep(self, keys):
		
		# Shapeshift
		timeSinceLastShift = (pygame.time.get_ticks() - self.lastShift)/1000.0

		if(timeSinceLastShift >= CONFIG.PLAYER_SHAPESHIFT_COOLDOWN):
		
			if(keys[pygame.K_SPACE]):
			
				#self.currentShape=random.randint(0,3)
				if ( self.currentShape < 3):
					self.currentShape += 1
				else:
					self.currentShape = 0
				
				if(self.currentShape == 0):
					self.currentPlayermode = PlayerHuman(self)
				elif(self.currentShape == 1):
					self.currentPlayermode = PlayerGepard(self)
				elif(self.currentShape == 2):
					self.currentPlayermode = PlayerSnake(self)
				elif(self.currentShape == 3):
					self.currentPlayermode = PlayerBird(self)
						
				print("Shift into shape " + str(self.currentShape))

				# reset action, so that the imglist will be reloaded
				# facial direction needs to be stored
				self.currentAction = "m" + self.currentAction[-1]

				# Cooldown
				self.lastShift = pygame.time.get_ticks()

			# end if
		# end if

		self.currentPlayermode.nextStep(keys)

		self.updateImageSet()
		
		MovableObject.nextStep(self)
		
# -----> Spam debug output !!!!!!!!!!!!!!!!!!!!!!!!!!!
		print("P: " + str(self.position) + " S: " + str(self.speed) + " - " + self.lastHCollision + " - " + self.lastVCollision)
		
		
	def updateImageSet(self):
		
		oldAction = self.currentAction
		
		# standing right
		if (self.speed == [0,0] and
				self.currentAction[0] != "s" and
				self.currentAction[-1] == "r"):
				
			self.currentAction = "sr"
			
			# stop the bird to standing during flight
			if(self.currentShape == 3 and not self.lastTickVelY >= 0):
				self.currentAction = "rr"
			
			
		# standing left
		if (self.speed == [0,0] and
				self.currentAction[0] != "s" and
				self.currentAction[-1] == "l"):

			self.currentAction = "sl"
			
			# stop the bird to standing during flight
			if(self.currentShape == 3 and not self.lastTickVelY >= 0):
				self.currentAction = "rl"
				print("stop")

		# running right
		if (self.speed[0] > 0 and
				self.speed[1] == 0 and
				self.currentAction != "rr"):

			self.currentAction = "rr"

		# running left
		if (self.speed[0] < 0 and
				self.speed[1] == 0 and
				self.currentAction != "rl"):

			self.currentAction = "rl"
	
		# jumping right
		if ((self.currentAction[1] == "r" or self.speed[0] > 0) and
				self.speed[1] != 0 and
				self.currentAction != "jr"):

			self.currentAction = "jr"
		
		# jumping left
		if ((self.currentAction[1] == "l" or self.speed[0] < 0) and
				self.speed[1] != 0 and
				self.currentAction != "jl"):

			self.currentAction = "jl"
		
		if (oldAction != self.currentAction):
			self.imglist = self.currentPlayermode.imagesets[self.currentAction]
			self.currentImg = self.imglist[0]
		
		self.lastTickVelY = self.currentPlayermode.lastTickVelY
		
		#print(self.currentAction)
