import pygame, os, random

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

		if (currentImg == None and not len(imglist) == 0):
			cimg_index = random.randint(0, len(imglist)-1)
			currentImg = imglist[cimg_index]
		self.currentImg = currentImg

	

	def nextStep(self):
		
		if(self.animated):
			self.nextFrame()

	
	# for animated objects: sets currentImg to next img in imglist
	def nextFrame(self):
		cimg_index = self.imglist.index(self.currentImg)
		
		if (cimg_index == len(self.imglist)-1):
			cimg_index = 0
		else:
			cimg_index += 1

		self.currentImg = self.imglist[cimg_index]
