import pygame, os

from WorldObject import WorldObject

import CONFIG

class MovableObject(WorldObject):
	
	speed = [0,0]
	maxSpeed = 0

	cboxT = None
	cboxB = None
	cboxL = None
	cboxR = None

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

		self.updateCollisionBox()


	# override: movable objects do need a more detailled
	# collision model
	def updateCollisionBox(self):

		
		self.cboxC = pygame.Rect(self.position[0] +
					CONFIG.LEGAL_OVERHANG,
				self.position[1],
				(self.hsize*CONFIG.TILE_WIDTH - 2 *
					CONFIG.LEGAL_OVERHANG),
				(self.vsize*CONFIG.TILE_HEIGHT))
		

		self.cboxT = pygame.Rect(self.cboxC.left,
				self.cboxC.top - CONFIG.CBOX_WIDTH,
				self.cboxC.right - self.cboxC.left,
				CONFIG.CBOX_WIDTH)
		self.cboxB = pygame.Rect(self.cboxC.left,
				self.cboxC.bottom,
				self.cboxC.right - self.cboxC.left,
				CONFIG.CBOX_WIDTH)
		self.cboxL = pygame.Rect(self.cboxC.left - CONFIG.CBOX_WIDTH,
				self.cboxC.top, 
				CONFIG.CBOX_WIDTH,
				self.cboxC.bottom - self.cboxC.top)
		self.cboxR = pygame.Rect(self.cboxC.right,
				self.cboxC.top,
				CONFIG.CBOX_WIDTH,
				self.cboxC.bottom - self.cboxC.top)
	
	
	def nextStep (self):
		
		WorldObject.nextStep(self)

		self.physicMove()
		
	def move (self, speed):
		
		self.position[0] += speed[0]
		self.position[1] += speed[1]

		self.updateCollisionBox()

	
	def physicMove (self):
		
		surrobjs = self.world.objSurr_H_static(self.position,
				CONFIG.RADIUS_COLLISION_CHECK)

		if (not self.canHover):
			self.speed[1] += CONFIG.GRAVITATION

		for obj in surrobjs:

			if ( not obj.collision ):
				continue

			# check, if the centerbox has already collided
			stuck = self.cboxC.colliderect(obj.cboxC)
			
			# collide at ground
			if (self.cboxB.colliderect(obj.cboxC)):
				if (self.speed[1] > 0):
					self.speed[1] = 0
				if (stuck):
					self.move([0,obj.cboxC.top - self.cboxC.bottom])
			# collide at cealing
			if (self.cboxT.colliderect(obj.cboxC)):
				if (self.speed[1] < 0):
					self.speed[1] = 0	
				if (stuck):
					self.move([0,obj.cboxC.bottom - self.cboxC.top])
			# collide left
			if (self.cboxL.colliderect(obj.cboxC)):
				if (self.speed[0] < 0):
					self.speed[0] = 0
				if (stuck):
					self.move([self.cboxC.left - obj.cboxC.right,0])
			# collide right
			if (self.cboxR.colliderect(obj.cboxC)):
				if (self.speed[0] > 0):
					self.speed[0] = 0
				if (stuck):
					self.move([obj.cboxC.left - self.cboxC.right,0])
			
		# end for (searching through all objects in range)
		
		self.move(self.speed)
		#end method physic movements

		
