import pygame, os, datetime, CONFIG



class PlayerHuman ():
	
	def __init__ (self, player):
		self.player = player
		self.player.maxSpeed=CONFIG.PLAYER_SPEED_HUMAN
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_HUMAN
		
	def nextStep(self,keys):
	
	# Mensch wird normal mit Pfeiltasten gesteuert, er bleibt stehen, wenn nichts gedrueckt wird
		
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.player.speed[0] = self.player.maxSpeed
			self.player.facingForward = True
		if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			self.player.speed[0] = -self.player.maxSpeed
			self.player.facingForward = False
			
		if(keys[pygame.K_UP]):
			self.player.speed[1] = -self.player.jumpSpeed
	
		print(self.player.speed)
	
	
	
class PlayerGepard ():
	
	def __init__ (self, player):
		self.player = player
		player.maxSpeed=CONFIG.PLAYER_SPEED_GEPARD
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_GEPARD
		
	def nextStep(self,keys):
	
	# Gepard bewegt sich immer vorwaerts, mit Pfeiltasten wird richtung veraendert
	
		if(self.player.facingForward):
			self.player.speed[0] = self.player.maxSpeed
		else:
			self.player.speed[0] = -self.player.maxSpeed
		
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.player.facingForward = True
		if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			self.player.facingForward = False
			
		if(keys[pygame.K_UP]):
			self.player.speed[1] = self.player.jumpSpeed
	
		print(self.player.speed)



class PlayerSnake ():
	
	def __init__ (self, player):
		self.player = player
		player.maxSpeed=CONFIG.PLAYER_SPEED_SNAKE
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_SNAKE
		
	def nextStep(self,keys):
		print("snake movement")
		
		
				
class PlayerBird ():
	
	def __init__ (self, player):
		self.player = player
		player.maxSpeed=CONFIG.PLAYER_SPEED_BIRD
		self.player.jumpSpeed=CONFIG.PLAYER_JUMP_SPEED_BIRD
		
	def nextStep(self,keys):
		print("bird movemend")


