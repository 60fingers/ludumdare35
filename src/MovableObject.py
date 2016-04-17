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
			frameDuration = frameDuration,
			currentImg = currentImg,
			hsize=hsize,
			vsize=vsize,
			visible = visible)

		self.speed = speed
		self.maxSpeed = maxSpeed
	
	def nextStep (self):
		
		WorldObject.nextStep(self)

		# gravitation!
		if (not canHover):
			self.speed[1] += CONFIG.GRAVITATION

		# predict new position
		self.position[0] += self.speed[0]
		self.position[1] += self.speed[1]


