import pygame, os
from  WorldObject import WorldObject

class StaticObject (WorldObject):

	def __init__(self,
			position,
			collision,
			imglist,
			animated,
			world,
			frameDuration=1,
			currentImg=None,
			visible=True):

		WorldObject.__init__(self,
				position=position,
				collision = collision,
				imglist = imglist,
				animated = animated,
				world = None,
				frameDuration = frameDuration,
				currentImg = currentImg,
				visible = visible)


class AirObject(StaticObject):
	
	def __init__(self, position):
		StaticObject.__init__(self, position,
			collision=False,
			imglist=[],
			animated=False,
			world=None,
			visible=False)

class GroundObject(StaticObject):
	
	def __init__(self, position):
		StaticObject.__init__(self, position,
			collision=True,
			imglist=["Ground1"],
			animated=False,
			world=None,
			visible=True)
			
class GroundDeepObject(StaticObject):
	
	def __init__(self, position):
		StaticObject.__init__(self, position,
			collision=True,
			imglist=["GroundDeep1"],
			animated=False,
			world=None,
			visible=True)

class WallObject(StaticObject):
	
	def __init__(self, position):
		StaticObject.__init__(self, position,
			collision=True,
			imglist=["Wall1", "Wall2"],
			animated=True,
			world=None,
			frameDuration=30,
			visible=True)
			
