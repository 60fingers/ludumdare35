import pygame, os

from WorldObject import WorldObject

import CONFIG

class MovableObject(WorldObject):
	
	speed = [0,0]
	maxSpeed = 0

	canHover = False

	def __init__ (self,
			position,
			collision,
			imglist,
			animated,
			world,			
			frameDuration = 1,
			currentImg = None,
			visible=True,
			hsize=1,
			vsize=1,
			conHover=False,
			speed=[0,0],
			maxSpeed=0):
	
		WorldObject.__init__(self,
			position = position,
			collision = collision,
			imglist = imglist,
			animated = animated,
			world = world,
			frameDuration = frameDuration,
			currentImg = currentImg,
			hsize=hsize,
			vsize=vsize,
			visible = visible)

		self.speed = speed
		self.maxSpeed = maxSpeed
		self.lastHCollision = "not h. blocked"
		self.lastVCollision = "not v. blocked"
	
	def nextStep (self):
		
		WorldObject.nextStep(self)

		# gravitation!
		if (not self.canHover):
			self.speed[1] += CONFIG.GRAVITATION

		self.updateRect()
		
		# moving to the new position axis after axis
		if(self.speed[0] != 0):
			self.lastHCollision = "not h. blocked"
			self.moveAndCheckX(self.world,self.speed[0])
		if(self.speed[1] != 0):
			self.lastVCollision = "not v. blocked"
			self.moveAndCheckY(self.world,self.speed[1])
		
		
		

	# moving on X axis with collision check
	def moveAndCheckX(self, world, speedx):
	
		# Move the rect first
		self.rect.left += speedx
		
		for obj in world.objectsSurrounding(self.position, CONFIG.RADIUS_COLLISION_CHECK):
			if (not obj.collision):
				continue
			
			obj.updateRect()
			
			if self.rect.colliderect(obj.rect):
				
				
				
				# Moving right and hit the left side of the object 
				# --> stand on the left side of the object
				
				if speedx > 0: 
					self.rect.left = obj.rect.left - (obj.hsize*CONFIG.TILE_WIDTH)
					self.speed[0] = 0
					self.lastHCollision = "right h. blocked"
					
				# Moving left and hit the right side of the object 
				# --> stand on the right side of the object
				elif speedx < 0:
					self.rect.left = obj.rect.right
					self.speed[0] = 0
					self.lastHCollision = "left h. blocked"
					
				
		#synchronise the rect position with the objects position
		self.position[0] = self.rect.left
		obj.updateRect()
	
	# moving on Y axis with collision check
	def moveAndCheckY(self, world, speedy):
	
		# Move the rect first
		self.rect.top += speedy
		
		for obj in world.objectsSurrounding(self.position, CONFIG.RADIUS_COLLISION_CHECK):
			if (not obj.collision):
				continue
			
			obj.updateRect()
			
			if self.rect.colliderect(obj.rect):
				
				obj.updateRect()
				
				# Moving down and hit the top side of the object 
				# --> stand on top of the object
				
				if speedy > 0:
					self.rect.bottom = obj.rect.top
					self.speed[1] = 0
					self.lastVCollision = "down v. blocked"
					
				# Moving up and hit the bottom side of the object 
				# --> stand below the object
				elif speedy < 0:
					self.rect.top = obj.rect.bottom
					self.speed[1] = 0
					self.lastVCollision = "up v. blocked"
				
				
		#synchronise the rect position with the objects position
		self.position[1] = self.rect.top
		obj.updateRect()