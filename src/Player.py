import pygame, os, datetime 

from MovableObject import MovableObject

class Player (MovableObject):
	
	def __init__ (self, position):
		MovableObject.__init__(self,
			position,
			collision=True,
			imglist=["player1", "player2"],
			animated=False,
			visible=True,
			maxSpeed=3)
			
		
	currentKeys = "" # leerer String, wird durch passenden String ersetzt
	lastKeys = "" # siehe oben
	lastKeyTime = "" # siehe oben, TODO welches Zeitformat verwenden wir hier?
	
