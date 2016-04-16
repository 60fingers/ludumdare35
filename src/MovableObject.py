import pygame, os

class MovableObject(WorldObject):
	
	def __init__ (self):
		self.speed = [0,0]
	
	def move (self):
		self.position[0] += self.speed[0]
		self.position[1] += self.speed[1]

