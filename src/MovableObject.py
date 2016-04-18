import pygame, os

from WorldObject import WorldObject

import CONFIG

class MovableObject(WorldObject):
	
	speed = [0,0]
	maxSpeed = 0

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

		if (not self.canHover):
			self.speed[1] += CONFIG.GRAVITATION

		ground = False
		
		for obj in surrobjs:

			if ( not obj.collision):
				continue
			
			if (self.cbox.colliderect(obj.cbox)):
				
				# the tolerance is needed because of the caving in
				if (self.cbox.top <= obj.cbox.top - CONFIG.TOLERANCE_HEADHEIGHT):

					# the player's coming from above or from above or from the side!
					
					if (self.cbox.bottom - self.speed[1] < obj.cbox.top):
						# landed on object - haha, lucky
						ground = True
						
						if (self.speed[1] > 0):
							self.speed[1] = 0

						# correct caving into ground - MUST be > 0
						if( self.cbox.bottom - obj.cbox.top > CONFIG.MAX_CAVING_IN):
							self.move([0, obj.cbox.top - self.cbox.bottom + CONFIG.MIN_CAVING_IN])
							
					else:
						# get out of the wall, you idiot!


						# ignore stubbing the toes						
						if (self.cbox.bottom - obj.cbox.top < CONFIG.MAX_STEP_HEIGHT):
							continue
						
						# ran into the wall on the right side
						if(self.cbox.left < obj.cbox.left):
							# move back left
							self.move([obj.cbox.left - self.cbox.right + CONFIG.MIN_CAVING_IN, 0])
							
							# prevent from running again
							if (self.speed[0] > 0):
								self.speed[0] = 0

						# ran into the wall on the left side
						elif(self.cbox.right > obj.cbox.right):
							# move back right	
							self.move([obj.cbox.right - self.cbox.left - CONFIG.MIN_CAVING_IN, 0])
							
							# prevent from running again
							if (self.speed[0] < 0):
								self.speed[0] = 0

					# end if (top or side)

				# end if (top or below)


				else:
					# now checking top

					crashfromrightbelow = False 	# hack...

					if (not self.speed[1] == 0):
						speedComponentRelation = float(self.speed[0]) / -self.speed[1]
					else:
						crashfromrightbelow = True

					crashvector = [0,0]
					
					crashedFromLeft = None

					# check, wether the crash was on the left or the right side
					if (self.cbox.left < obj.cbox.left):

						#crashed from left
						crashedFromLeft = True
						crashvector[0] = self.cbox.right - obj.cbox.left

					else:
						
						#crashed from right
						crashedFromLeft = False
						crashvector[0] = self.cbox.left - obj.cbox.right

					# end if


					crashvector[1] = obj.cbox.bottom - self.cbox.top

					if (not crashvector[1] == 0):
						crashComponentRelation = float(crashvector[0]) / crashvector[1]
					else:
						crashComponentRelation = 99999 # another huge number


					# check if the player crashed into the ceiling or into the wall
					if (speedComponentRelation > crashComponentRelation 
							and not crashfromrightbelow):
						
						# horizontal correction
						if (crashedFromLeft):
							
							self.move([obj.cbox.left - self.cbox.right + CONFIG.MIN_CAVING_IN, 0])

						else:
							
							self.move([obj.cbox.right - self.cbox.left - CONFIG.MIN_CAVING_IN, 0])


						self.speed[0] = 0

					else:
						
						# vertical correction
						
						self.move([0, obj.cbox.bottom - self.cbox.top])
						self.speed[1] = 0



			# end if (is there even collision)
			
		# end for (searching through all objects in range)
			
		
		self.move(self.speed)
		#end method physic movements

		
