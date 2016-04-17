import pygame, os, CONFIG



class PlayerHuman ():
	
	def __init__ (self, player):

		self.player = player
		self.player.hsize = 1
		self.player.vsize = 2
		self.player.maxSpeed=CONFIG.PLAYER_SPEED_HUMAN
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_HUMAN
		

	def nextStep(self,keys):
	
		#  Der Mensch wird normal mit Pfeiltasten gesteuert,
		#  er bleibt stehen, wenn nichts gedrueckt wird
		
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.player.speed[0] = self.player.maxSpeed
			self.player.facingForward = True
			
		elif(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			self.player.speed[0] = -self.player.maxSpeed
			self.player.facingForward = False
			
		else:	
			self.player.speed[0] = 0
		
		if(keys[pygame.K_UP] and (self.player.speed[1] == 0)):
			self.player.speed[1] = -self.player.jumpSpeed
			self.lastJumpInput = pygame.time.get_ticks()
	
	
		print(str(self.player.speed) + " as Human")
	
#-------------------------------------------------------------------
	
class PlayerGepard ():
	
	def __init__ (self, player):
		self.player = player
		self.player.hsize = 2
		self.player.vsize = 1
		player.maxSpeed=CONFIG.PLAYER_SPEED_GEPARD
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_GEPARD
		
	def nextStep(self,keys):
	
		#  Der Gepard bewegt sich immer vorwaerts, mit Pfeil-
		#  tasten wird richtung veraendert
	
		if(self.player.facingForward):
			self.player.speed[0] = self.player.maxSpeed
		else:
			self.player.speed[0] = -self.player.maxSpeed
		
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.player.facingForward = True
			
		if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			self.player.facingForward = False
			
		if(keys[pygame.K_UP] and (self.player.speed[1] == 0)):
			self.player.speed[1] = self.player.jumpSpeed
	
		print(str(self.player.speed) + " as Gepard")

#-------------------------------------------------------------------

class PlayerSnake ():
	
	def __init__ (self, player):

		self.player = player
		self.player.hsize = 1
		self.player.vsize = 1
		self.player.maxSpeed=CONFIG.PLAYER_SPEED_SNAKE
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_SNAKE

		self.leftArrowNext = False
		self.lastDirectionInput = 0
		
	def nextStep(self,keys):
	
		#  Bei der Schlange muessen die Richtungstasten immer
		#  abwechselnd gedruekt werden, um vorran zu kommen.
		#  Die Schlange wechselt im Sprung die Richtung
		
	
		# right arrow key
		if (keys[pygame.K_RIGHT] and
				not keys[pygame.K_LEFT] and
				not self.leftArrowNext):

			if(self.player.facingForward):
				self.player.speed[0] = self.player.maxSpeed
				
			else:
				self.player.speed[0] = -self.player.maxSpeed
			

			self.lastDirectionInput = pygame.time.get_ticks()
			self.leftArrowNext = True
			

		# left arrow key
		elif (keys[pygame.K_LEFT] and 
				not keys[pygame.K_RIGHT] and
				self.leftArrowNext):

			if (self.player.facingForward):
				self.player.speed[0] = self.player.maxSpeed

			else:
				self.player.speed[0] = -self.player.maxSpeed
				

			self.lastDirectionInput = pygame.time.get_ticks()
			self.leftArrowNext = False
			

		# nothing pressed, stopping after 0.1s. If it would stop right away,
		# the player would need to spam arrow buttons
		else:
			if (((pygame.time.get_ticks() - self.lastDirectionInput)) > 100 ):
				self.player.speed[0] = 0
		

		# jump to flip move direction
		if (keys[pygame.K_UP] and 
				(self.player.speed[1] == 0)):

			self.player.speed[1] = -self.player.jumpSpeed
			self.player.facingForward =  (not self.player.facingForward)
			
		
		print(str(self.player.speed) + " as Snake")
		
#------------------------------------------------------------------		
				
class PlayerBird ():
	
	def __init__ (self, player):

		self.player = player
		self.player.hsize = 1
		self.player.vsize = 1
		self.player.maxSpeed=CONFIG.PLAYER_SPEED_BIRD
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_BIRD
		
		self.lastJumpInput = 0
		
	def nextStep(self,keys):
	
		#  Der Vogel bewegt sich nur wenn er in der Luft ist.
		#  Mit Richtungstasten wird die Richtung geaendert und
		#  mit statt zu springen kann er mit Fluegelschlagen 
		#  an Hoehe gewinnen. Er kann nur am Boden stehenbleiben
		
		# forward, in the air
		if (self.player.facingForward and
				(self.player.speed[1] != 0) ):

			self.player.speed[0] = self.player.maxSpeed
			
		# backward, in the air
		elif ( not self.player.facingForward and
				(self.player.speed[1] != 0) ):

			self.player.speed[0] = -self.player.maxSpeed

		# standing still
		else:
			self.player.speed[0] = 0


		# turn right
		if (keys[pygame.K_RIGHT] and 
				not keys[pygame.K_LEFT]):

			self.player.facingForward = True
			
		# turn left
		if (keys[pygame.K_LEFT] and 
				not keys[pygame.K_RIGHT]):

			self.player.facingForward = False
						

		# cooldown for jump
		timeSinceLastJump = (pygame.time.get_ticks() - self.lastJumpInput)/1000

		if (keys[pygame.K_UP] and
				(timeSinceLastJump >= CONFIG.PLAYER_BIRD_FLAP_COOLDOWN)):
		
			self.player.speed[1] = -self.player.jumpSpeed
			self.lastJumpInput = pygame.time.get_ticks()
			
		print(str(self.player.speed) + " as Bird")


