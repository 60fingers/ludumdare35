import pygame, os, random

import CONFIG

class WorldObject:

	position = None
	collision = None
	imglist = []
	animated = False
	frameDuration = 1
	curFrameTime = 0
	visible = True
	currentImg = None
	imgAdjustV = 0
	imgAdjustH = 0

	# size measured in tiles
	hsize = 1
	vsize = 1

	def __init__(self,
			position,
			collision,
			imglist,
			animated,
			world,
			frameDuration=1,
			currentImg=None,
			imgAdjustV=0,
			imgAdjustH=0,
			hsize=1,
			vsize=1,
			visible=True):

		self.position = position
		self.collision = collision
		self.imglist = imglist
		self.animated = animated
		self.world = world
		self.frameDuration = frameDuration
		self.visible = visible

		self.imgAdjustV = imgAdjustV
		self.imgAdjustH = imgAdjustH

		self.updateCollisionBox()

		# choose an image from imagelist randomly -> for variation
		if (currentImg == None and not len(imglist) == 0):
			cimg_index = random.randint(0, len(imglist)-1)
			currentImg = imglist[cimg_index]
		self.currentImg = currentImg

		# choose a current frame time randomly ->
		# global sync. animation would look like crap
		self.curFrameTime = random.randint(0,frameDuration-1)	

	def updateCollisionBox(self):
		self.cboxC = pygame.Rect(self.position[0],
				self.position[1],
				(self.hsize*CONFIG.TILE_WIDTH),
				(self.vsize*CONFIG.TILE_HEIGHT))
	
	def nextStep(self):
		
		if(self.animated):
			self.nextFrame()

	
	# for animated objects: sets currentImg to next img in imglist
	def nextFrame(self):
		
		self.curFrameTime += 1
		
		# current frame had it's time, next one please
		if (self.curFrameTime >= self.frameDuration):

			cimg_index = self.imglist.index(self.currentImg)
			
			if (cimg_index == len(self.imglist)-1):
				cimg_index = 0
			else:
				cimg_index += 1

			self.currentImg = self.imglist[cimg_index]

			self.curFrameTime = 0
		
		#end if
	
	
