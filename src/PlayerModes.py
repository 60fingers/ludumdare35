import pygame, os, datetime, CONFIG



class PlayerHuman ():
	
	def __init__ (self, player):
		self.player = player
		player.maxSpeed=CONFIG.PLAYER_SPEED_HUMAN
		
	def nextStep(self,keys):
	
		if(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
			self.position[0] += self.maxSpeed
		if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
			self.position[0] -= self.maxSpeed
		if(keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
			self.position[1] -= self.maxSpeed
		if(keys[pygame.K_DOWN] and not keys[pygame.K_UP]):
			self.position[1] += self.maxSpeed
	
	
	
	
	
class PlayerGepard ():
	
	def __init__ (self, player):
		self.player = player
		player.maxSpeed=CONFIG.PLAYER_SPEED_GEPARD
		
	def nextStep(self,keys):
		print("not implemented")



class PlayerSnake ():
	
	def __init__ (self, player):
		self.player = player
		player.maxSpeed=CONFIG.PLAYER_SPEED_SNAKE
		
	def nextStep(self,keys):
		print("not implemented")
		
		
				
class PlayerBird ():
	
	def __init__ (self, player):
		self.player = player
		player.maxSpeed=CONFIG.PLAYER_SPEED_BIRD
		
	def nextStep(self,keys):
		print("not implemented")


