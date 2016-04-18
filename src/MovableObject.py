import pygame, os

from WorldObject import WorldObject

import CONFIG

class MovableObject(WorldObject):
	
	speed = [0,0]
	maxSpeed = 0
	coll = " "
	groundBefore

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
		self.lastHCollision = "not h. blocked"
		self.lastVCollision = "not v. blocked"
	
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

		self.move(self.speed)

		nowground = False
		
		for obj in surrobjs:

			if ( not obj.collision):
				continue
			
			if (self.cbox.colliderect(obj.cbox)):
				
				if (self.cbox.top <= obj.cbox.top):

					# from above or from the side!
					
					if (self.cbox.bottom - self.speed[1] > obj.cbox.top):
						nowground = True
						
						self.coll = "down"
						# landed on object - haha, lucky
						self.move([0, obj.cbox.top - self.cbox.bottom ])
						self.speed[1] = 0
					
					else:
						# get out of the wall, you idiot!

						self.speed[0] = 0
						
						if(self.cbox.left < obj.cbox.left):
							self.coll = "right"
							# move back left
							self.move([obj.cbox.left - self.cbox.right, 0])

						elif(self.cbox.right > obj.cbox.right):
							self.coll = "left"
							# move back right	
							self.move([obj.cbox.right - self.cbox.left, 0])
					# end if
				# end if
			# end if
			
		# end for
		
		if (not nowground):
			# gravitation!
			if (not self.canHover):
				self.speed[1] += CONFIG.GRAVITATION
		
		#end method physic movements

		





