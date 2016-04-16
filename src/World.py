import pygame, os
from Player import Player
from StaticObject import *
from MovableObject import *

from WorldReader import WorldReader


class World:

	player = None
	movables = []
	stativs = []
	
	def __init__(self):
		worldobjects = WorldReader().readImage("../maps/world1stat.png","../maps/world1mov.png")
		self.movables = worldobjects[0]
		self.statics = worldobjects[1]
		#TODO: test wich values to take
		self.levelheight = 10
		self.surroundarea = 10

		self.player = Player([0,0])	# TODO echte Spielerposition verwenden!
	
	def objectsSurrounding(self,position):
		surroundings = []
		x = position[0]
		# add every static object in range
		i = ((x*self.levelheight) - self.surroundarea)
		while i < ((x*self.levelheight) + self.surroundarea):
			surroundings.append(self.movables[i])
			i+=1
		
		# add every movable object in range
		for m in self.movables:
			if m.position[0] >= (x - self.surroundarea) & m.position[0] <= (x + self.surroundarea):
				surroundings.append(m)
			
		return surroundings
		
	def nextStep(self,keys):
		print("not implemented")
