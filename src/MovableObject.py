import pygame, os

from WorldObject import WorldObject

class MovableObject(WorldObject):
	
	speed = [0,0]
	maxSpeed = 0

	def __init__ (self, position, collision,
			imglist, animated, maxSpeed=0,
			visible=True, speed=[0,0]):
	
		WorldObject.__init__(self, position, collision,
			imglist, animated, visible)

		self.speed = speed
		self.maxSpeed = maxSpeed
	
	def move (self):
		self.position[0] += self.speed[0]
		self.position[1] += self.speed[1]

