import pygame, os

class World:

	def __init__(self):
		self movables = ""
		self statics = ""
		#TODO: test wich values to take
		self levelheight = 10
		self surroundarea = 10
	
	def objectsSurrounding(self,position):
		surroundings = []
		x = position[0]
		# add every static object in range
		i = ((x*levelheight) - surroundarea)
		while i < ((x*levelheight) + surroundarea):
			surroundings.append(movables[i])
			i++
		
		# add every movable object in range
		for m in movables:
			if m.position[0] >= (x - surroundarea) & m.position[0] <= (x + surroundarea):
				surroundings.append(m)
			
		return surroundings
		
	def nextStep(self,keys):
		print("not implemented")