import pygame, os

class WorldObject:

	def __init__(self, position, collision, imglist, animated, visible=True):
		#print("created new world object")
		self.position = position
		self.collision = collision
		self.imglist = imglist
		self.animated = animated
		self.visible = visible
		self.currentImg = None

	

	def nextStep(self):
		print("worldobject: next step")
