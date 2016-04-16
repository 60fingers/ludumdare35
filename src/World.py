import pygame, os
from WorldReader import WorldReader

class World:

	player = None
	movables = []
	stativs = []
	#TODO: test wich values to take
	levelheight = 10
	surroundarea = 10

	def __init__(self):
		worldobjects = WorldReader().readImage("../maps/world1stat.png","../maps/world1mov.png")
		self.movables = ""
		self.statics = ""
	
	def objectsSurrounding(self,position):
		surroundings = []
		x = position[0]
		# add every static object in range
		i = ((x*levelheight) - surroundarea)
		while i < ((x*levelheight) + surroundarea):
			surroundings.append(movables[i])
			i+=1
		
		# add every movable object in range
		for m in movables:
			if m.position[0] >= (x - surroundarea) & m.position[0] <= (x + surroundarea):
				surroundings.append(m)
			
		return surroundings
		
	def nextStep(self,keys):
		print("not implemented")
