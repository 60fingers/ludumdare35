import pygame, os

class WorldObject:

	position = None
	collision = None
	imglist = []
	animated = False
	visible = True
	currentImg = None

	def __init__(self, position, collision, imglist, animated, currentImg=None, visible=True):
		#print("created new world object")
		self.position = position
		self.collision = collision
		self.imglist = imglist
		self.animated = animated
		self.visible = visible
		self.currentImg = currentImg

	

	def nextStep(self):
		print("worldobject: next step")
