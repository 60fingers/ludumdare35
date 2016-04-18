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
			canHover=False,
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

		self.updateCollisionBox()
		
		# moving to the new position axis after axis
		if(self.speed[0] != 0):
			self.lastHCollision = "not h. blocked"
			self.moveAndCheckY(self.world,self.speed[1])
		if(self.speed[1] != 0):
			self.lastVCollision = "not v. blocked"
			self.moveAndCheckX(self.world,self.speed[0])
	
	def move  (self):
		
		print("not implemented")





