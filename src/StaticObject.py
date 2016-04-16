import pygame, os
from  WorldObject import WorldObject

class StaticObject (WorldObject):

	def __init__(self, position, collision, imglist, animated, visible=True):
		super(StaticObject, self).__init__(position, collision, imglist, animated, visible)


class AirObject(StaticObject):
	
	def __init__(self, position):
		super(AirObject, self).__init__(position,
			collision=False,
			imglist=[],
			animated=False,
			visible=False)

class GroundObject(StaticObject):
	
	def __init__(self, position):
		super(WallObject, self).__init__(position,
			collision=True,
			imglist=["ground1", "ground2"]
			animated=False,
			visible=True)

class WallObject(StaticObject):
	
	def __init__(self, position):
		super(StaticObject, self).__init__(position,
			collision=True,
			imglist=["wall1", "wall2"]
			animated=False,
			visible=True)
			
