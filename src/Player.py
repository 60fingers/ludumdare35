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
			
		#self.vsize = 1
		#self.hsize = 2
		self.canHover = False
			
		self.lastShift = -1 # cooldown timer
		self.currentShape = 0 # Shapes 0=human, 1=gepard, 2=snake, 3=bird
		self.shapeString = "Human"
		self.currentPlayermode = PlayerHuman(self)
		self.jumpSpeed = CONFIG.PLAYER_JUMP_SPEED_HUMAN
		self.facingForward = True
		self.lastTickVelY = 0
		self.dead = False
		self.timeOfDead = 0
		
		self.currentAction = "sr" # possible: jr, jl, rl, rr, sr, sl
		
		
	
	def nextStep(self, keys):
		
		# Shapeshift
		timeSinceLastShift = (pygame.time.get_ticks() - self.lastShift)

		if(timeSinceLastShift >= CONFIG.PLAYER_SHAPESHIFT_COOLDOWN):
		
			if(keys[pygame.K_SPACE]):
			
				#self.currentShape=random.randint(0,3)
				if ( self.currentShape < 3):
					self.currentShape += 1
				else:
					self.currentShape = 0
				
				if(self.currentShape == 0):
					self.currentPlayermode = PlayerHuman(self)
					self.shapeString = "Human"
					self.world.sounds["Fight1"].play()
				elif(self.currentShape == 1):
					self.currentPlayermode = PlayerGepard(self)
					self.shapeString = "Gepard"
					self.world.sounds["ShiftGepard"].play()
				elif(self.currentShape == 2):
					self.currentPlayermode = PlayerSnake(self)
					self.shapeString = "Snake"
					self.world.sounds["ShiftSnake"].play()
				elif(self.currentShape == 3):
					self.currentPlayermode = PlayerBird(self)
					self.shapeString = "Bird"
					self.world.sounds["ShiftEagle"].play()
						
				print("Shift into shape " + str(self.currentShape))

				# reset action, so that the imglist will be reloaded
				# facial direction needs to be stored
				self.currentAction = "m" + self.currentAction[-1]

				# Cooldown
				self.lastShift = pygame.time.get_ticks()

			# end if
		# end if

		self.updateImageSet()

		MovableObject.nextStep(self)

		self.currentPlayermode.nextStep(keys)
		
		# Die if under the world
		if(self.position[1] >= 799 and not self.dead):
			self.world.sounds["Death"].play()
			self.dead = True
			self.timeOfDead = pygame.time.get_ticks()
		
		# revive after 5 sec on top of the level
		if(self.dead == True and pygame.time.get_ticks() - self.timeOfDead > 5000):
			self.dead = False
			self.position[1] = 2
			
		
	def updateImageSet(self):
		
		oldAction = self.currentAction
		
		# standing right
		if (self.speed == [0,0] and
				#self.currentAction[0] != "s" and
				#self.currentAction[-1] == "r"):
				self.facingForward):
				
			self.currentAction = "sr"
			
			# stop the bird to standing during flight
			if(self.currentShape == 3 and not self.lastTickVelY >= 0):
				self.currentAction = "rr"
			
			
		# standing left
		if (self.speed == [0,0] and
				#self.currentAction[0] != "s" and
				#self.currentAction[-1] == "l"):
				not self.facingForward):
			self.currentAction = "sl"
			
			# stop the bird to standing during flight
			if(self.currentShape == 3 and not self.lastTickVelY >= 0):
				self.currentAction = "rl"

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
		
		# flap
		if(self.currentShape == 3):
			if(self.currentPlayermode.lastWasFlap):
				if(self.facingForward):
					self.currentAction = "fr"
				else:
					self.currentAction = "fl"
		
		if (oldAction != self.currentAction):
			self.imglist = self.currentPlayermode.imagesets[self.currentAction]
			self.currentImg = self.imglist[0]
		
		self.lastTickVelY = self.currentPlayermode.lastTickVelY
		
		#print(self.currentAction)

	# override, make player slim
	def updateCollisionBox(self):
		self.cbox = pygame.Rect(self.position[0] + CONFIG.LEGAL_OVERHANG,
				self.position[1],
				(self.hsize*CONFIG.TILE_WIDTH - 2 * CONFIG.LEGAL_OVERHANG),
				(self.vsize*CONFIG.TILE_HEIGHT))

