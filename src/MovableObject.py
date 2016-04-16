import pygame, os

from MovableObject import MovableObject

class MovableObject(WorldObject):
	
	speed = [0,0]

	def __init__ (self, position, collision, imglist, animated, visible=True):
		super(MovableObject).__init__(position, collision, imglist, animated, visible)
		self.speed = [0,0]
	
	def move (self):
		self.position[0] += self.speed[0]
		self.position[1] += self.speed[1]

