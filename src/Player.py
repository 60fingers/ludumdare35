import pygame, os, datetime 

from MovableObject import MovableObject

import CONFIG

class Player (MovableObject):
			
	currentKeys = "" # leerer String, wird durch passenden String ersetzt
	lastKeys = "" # siehe oben
	lastKeyTime = "" # siehe oben, TODO welches Zeitformat verwenden wir hier?	

	def __init__ (self, position):
		MovableObject.__init__(self,
			position,
			collision=True,
			imglist=["player1", "player2"],
			animated=False,
			visible=True,
			maxSpeed=CONFIG.PLAYER_SPEED_HUMAN)
	
	def nextStep(self, keys):
		a = int(3.14) # TODO bullshit to enable method
			

