import pygame, os
from  WorldObject import WorldObject

class StaticObject (WorldObject):

	def __init__(self, position, collision, imglist, animated, currentImg=None, visible=True):
		WorldObject.__init__(self, position, collision, imglist, animated, currentImg, visible)


class AirObject(StaticObject):
	
	def __init__(self, position):
		StaticObject.__init__(self, position,
			collision=False,
			imglist=[],
			animated=False,
			visible=False)

class GroundObject(StaticObject):
	
	def __init__(self, position):
		StaticObject.__init__(self, position,
			collision=True,
			imglist=["Ground1"],
			animated=False,
			visible=True)

class WallObject(StaticObject):
	
	def __init__(self, position):
		StaticObject.__init__(self, position,
			collision=True,
			imglist=["Wall1", "Wall2"],
			animated=True,
			visible=True)
			
