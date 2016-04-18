import pygame, os, CONFIG, random



class PlayerHuman ():
	
	def __init__ (self, player):

		self.player = player
		self.player.hsize = 1
		self.player.vsize = 2
		self.player.maxSpeed=CONFIG.PLAYER_SPEED_HUMAN
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_HUMAN
		self.lastTickVelY = 0
		
		self.imagesets = {
			"sr" : ["PlayerStandingRight"],
			"sl" : ["PlayerStandingLeft"],
			"rr" : ["PlayerRunningRight1",
					"PlayerRunningRight2"],
			"rl" : ["PlayerRunningLeft1",
					"PlayerRunningLeft2"],
			"jr" : ["PlayerJumpingRight"],
			"jl" : ["PlayerJumpingLeft"]}

		self.time_last_jump = 0

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
		

		time_since_last_jump = pygame.time.get_ticks() - self.time_last_jump

		if(keys[pygame.K_UP] and (self.player.speed[1] == 0)
				and (self.lastTickVelY >= 0) 
				and time_since_last_jump >= CONFIG.PLAYER_JUMP_COOLDOWN_HUMAN ):

			self.player.speed[1] = -self.player.jumpSpeed
			
			self.time_last_jump = pygame.time.get_ticks()

			r=random.randint(0,1)
			if(r == 0):
				self.player.world.sounds["JumpHuman1"].play()
			if(r == 1):
				self.player.world.sounds["JumpHuman2"].play()
					
		
		#for debugging
		if(keys[pygame.K_DOWN] and self.player.canHover ):
			self.player.speed[1] = self.player.jumpSpeed
		
		
		self.lastTickVelY = self.player.speed[1]
		
		# stop sticking on the upper border  
		if(self.player.position[1] == 0):
			self.player.speed[1] = 1
			self.lastTickVelY = -1
		
		#print(str(self.player.speed) + " as Human")
	
#-------------------------------------------------------------------

	
class PlayerGepard ():
	
	def __init__ (self, player):
		self.player = player
		self.player.hsize = 2
		self.player.vsize = 1
		player.maxSpeed=CONFIG.PLAYER_SPEED_GEPARD
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_GEPARD
		self.lastTickVelY = 0
		
		self.imagesets = {
			"sr" : ["GepardStandingRight"],
			"sl" : ["GepardStandingLeft"],
			"rr" : ["GepardRunningRight1"],
			"rl" : ["GepardRunningLeft1"],
			"jr" : ["GepardJumpingRight"],
			"jl" : ["GepardJumpingLeft"]}


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
			
		if(keys[pygame.K_UP] and (self.player.speed[1] == 0) and (self.lastTickVelY >= 0) ):
			self.player.speed[1] = -self.player.jumpSpeed
			self.lastJumpInput = pygame.time.get_ticks()
	
		self.lastTickVelY = self.player.speed[1]
		
		# stop sticking on the upper border  
		if(self.player.position[1] == 0):
			self.player.speed[1] = -1
			self.lastTickVelY = 1
			
		#print(str(self.player.speed) + " as Gepard")

#-------------------------------------------------------------------

class PlayerSnake ():
	
	def __init__ (self, player):

		self.player = player
		self.player.hsize = 1
		self.player.vsize = 1
		self.player.maxSpeed=CONFIG.PLAYER_SPEED_SNAKE
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_SNAKE
		self.lastTickVelY = 0

		self.leftArrowNext = False
		self.lastDirectionInput = 0
		
		self.imagesets = {
			"sr" : ["SnakeStandingRight"],
			"sl" : ["SnakeStandingLeft"],
			"rr" : ["SnakeMovingRight"],
			"rl" : ["SnakeMovingLeft"],
			"jr" : ["SnakeJumping"],
			"jl" : ["SnakeJumping"]}


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
				(self.player.speed[1] == 0) and (self.lastTickVelY >= 0)):

			self.player.speed[1] = -self.player.jumpSpeed
			self.player.facingForward =  (not self.player.facingForward)
			
		self.lastTickVelY = self.player.speed[1]
		
		# stop sticking on the upper border  
		if(self.player.position[1] == 0):
			self.player.speed[1] = -1
			self.lastTickVelY = 1
		
		#print(str(self.player.speed) + " as Snake")
		
#------------------------------------------------------------------		
				
class PlayerBird ():
	
	def __init__ (self, player):

		self.player = player
		self.player.hsize = 1
		self.player.vsize = 1
		self.player.maxSpeed=CONFIG.PLAYER_SPEED_BIRD
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_BIRD
		self.lastTickVelY = 0
		self.lastWasFlap = False
		self.timeSinceLastFlap = 0
		
		self.lastJumpInput = 0
	
		self.imagesets = {
			"sr" : ["BirdStandRight"],
			"sl" : ["BirdStandLeft"],
			"rr" : ["BirdGlideRight"],
			"rl" : ["BirdGlideLeft"],
			"jr" : ["BirdGlideRight"],
			"jl" : ["BirdGlideLeft"],
			"fr" : ["BirdFlapRight"],
			"fl" : ["BirdFlapLeft"]}


		
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
		timeSinceLastJump = (pygame.time.get_ticks() - self.lastJumpInput)

		# gravitation reduction
		if(self.player.speed[1] != 0):
			self.player.speed[1] -= int(0.5 * CONFIG.GRAVITATION) 
		
		if (keys[pygame.K_UP] and
				(timeSinceLastJump >= CONFIG.PLAYER_BIRD_FLAP_COOLDOWN)):
		
			self.player.speed[1] = -self.player.jumpSpeed
			self.lastJumpInput = pygame.time.get_ticks()
			self.lastWasFlap = True
			self.timeSinceLastFlap = 0
			
			r=random.randint(0,2)
			if(r == 0):
				self.player.world.sounds["MoveEagle1"].play()
			if(r == 1):
				self.player.world.sounds["MoveEagle2"].play()
			if(r == 2):
				self.player.world.sounds["MoveEagle3"].play()
					
		
		self.timeSinceLastFlap = (pygame.time.get_ticks() - self.lastJumpInput)
		
		if (self.timeSinceLastFlap > 150):
			self.lastWasFlap = False
		
		self.lastTickVelY = self.player.speed[1]
		
		# stop sticking on the upper border  
		if(self.player.position[1] == 0):
			self.player.speed[1] = -1
			self.lastTickVelY = 1
		
		#print(str(self.player.speed) + " as Bird")


