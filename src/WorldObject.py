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

	# size measured in tiles
	hsize = 1
	vsize = 1

	def __init__(self,
			position,
			collision,
			imglist,
			animated, 
			frameDuration=1,
			currentImg=None,
			hsize=1,
			vsize=1,
			visible=True):

		self.position = position
		self.collision = collision
		self.imglist = imglist
		self.animated = animated
		self.frameDuration = frameDuration
		self.visible = visible

		# choose an image from imagelist randomly -> for variation
		if (currentImg == None and not len(imglist) == 0):
			cimg_index = random.randint(0, len(imglist)-1)
			currentImg = imglist[cimg_index]
		self.currentImg = currentImg

		# choose a current frame time randomly -> global sync. animation would look like crap
		self.curFrameTime = random.randint(0,frameDuration-1)	

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
	
	def leftBounding(self):
		return self.position[0]
	
	def rightBounding(self):
		return self.position[0] + self.hsize * CONFIG.TILE_WIDTH

	def upperBounding(self):
		return self.position[1]
	
	def lowerBounding(self):
		return self.position[1] + self.vsize * CONFIG.TILE_HEIGHT
		
		
	# returns the overlapping pixels to a second world object on all 4 sides
	def overlappingScore(self, wobj):
		
		scores = { 	"t" : 0,
					"b" : 0,
					"l" : 0,
					"r" : 0}

		# collision scores horizontal
		if (self.leftBounding() < wobj.rightBounding() and
				self.leftBounding() > wobj.leftBounding()):

			scores["l"] = wobj.rightBounding() - self.leftBounding()

		elif(self.rightBounding() < wobj.rightBounding() and
				self.rightBounding() > wobj.leftBounding()):

			scores["r"] = self.rightBounding() - wobj.leftBounding()

		# collision scores vertical
		if (self.upperBounding() < wobj.upperBounding() and
				self.upperBounding() > wobj.lowerBounding()):

			scores["t"] = wobj.lowerBounding() - self.upperBounding()

		elif(self.lowerBounding() > wobj.upperBounding() and
				self.lowerBounding() < wobj.lowerBounding()):

			scores["b"] = self.lowerBounding() - wobj.upperBounding()

		return scores

	
	def correctOverlapping(self, wobj):
	
		scores = self.overlappingScore(wobj)

		count = 0
		
		for s in scores:
			if (scores[s] > 0):
				count += 1

		if (count < 2):
			return

		if ( scores["t"] > 0):
			
			# collision top
			
			if (scores["l"] > 0):
				
				# collision left

				if (scores["t"] > scores["l"]):
					self.speed[0] = 0
					self.position[0] = wobj.rightBounding()
				else:
					self.speed[1] = 0
					self.position[1] = wobj.lowerBounding()

			else:
				
				# collision right
				
				if (scores["t"] > scores["r"]):
					self.speed[0] = 0
					self.position[0] = wobj.leftBounding()
				else:
					self.speed[1] = 0
					self.position[1] = wobj.lowerBounding()						

		else:

			# collision bottom
			
			if (scores["l"] > 0):
				
				# collision left

				if (scores["b"] > scores["l"]):
					self.speed[0] = 0
					self.position[0] = wobj.rightBounding()
				else:
					self.speed[1] = 0
					self.position[1] = wobj.upperBounding()

			else:
				
				# collision right
				
				if (scores["b"] > scores["r"]):
					self.speed[0] = 0
					self.position[0] = wobj.leftBounding()
				else:
					self.speed[1] = 0
					self.position[1] = wobj.upperBounding()
		
		# end finding collision side
	
	# end collision check



