import pygame, os
import WorldObject from WorldObject

class StaticObject (WorldObject):

	def __init__(self, position, collision, imglist, animated, visible=True):
		super(StaticObject, self).__init__(position, collision, imglist, animated, visible)

