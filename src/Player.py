import pygame, os, datetime 

class Player (MovableObject):
	
	def __init__ (self):
		self.currentKeys = "" # leerer String, wird durch passenden String ersetzt
		self.lastKeys = "" # siehe oben
		self.lastKeyTime = "" # siehe oben, TODO welches Zeitformat verwenden wir hier?
	
