import pygame, os, datetime 

class Player (MovableObject):
	
	def __init__ (self):
		
	currentKeys = "" # leerer String, wird durch passenden String ersetzt
	lastKeys = "" # siehe oben
	lastKeyTime = "" # siehe oben, TODO welches Zeitformat verwenden wir hier?
	
