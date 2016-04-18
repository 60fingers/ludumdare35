import os, sys, pygame

import CONFIG

class HUD():
	
	def __init__(self, worldview):
		
		self.worldview = worldview
		self.elements = []
		self.font = pygame.font.SysFont("monospace", 15, bold = True)

		self.elements.append(
				MorphCoolDownBar(self,(50,50))
				)
				
		self.elements.append(
				DebugElement(self,(700,50))
				)
	
	def show(self):
	
		for e in self.elements:
			e.show()




class HUD_Element:

	size = (0,0)
	
	def __init__(self,
			hud,
			position,
			size,
			visible = True):
		
		self.hud = hud
		self.world = hud.worldview.world
		self.screen = hud.worldview.screen
		self.position = position
		self.visible = visible
		
		
		self.surf = pygame.Surface(size, pygame.SRCALPHA, 32)
	
	def show(self):
		
		if(self.visible):
			self.screen.blit(self.surf, self.position)

	def clear(self):
		self.surf = pygame.Surface(self.size, pygame.SRCALPHA, 32)
		
	#end class HUD_Element


	
#for demonstration
class AbstractUIElement(HUD_Element):
	
	# take this constructor header
	def __init__(self,
			hud,
			position,
			visible = True):
		
		#define a size
		self.size = (100,100)
		
		#take this line
		HUD_Element.__init__(self, hud, position,
				self.size, visible)
	
	#override show method
	def show(self):
		
		#clear surf
		self.clear()
		
		# draw your ui on self.surf
		label = self.hud.font.render("abstract ui element", 1, (5,5,5))
		self.surf.blit(label,(0,0))
		
		# call super show
		HUD_Element.show(self)
		
	#end class abstract ui element

	
class MorphCoolDownBar(HUD_Element):

	def __init__(self,
			hud,
			position,
			visible = True):
		
		self.borderwidth = 20
		self.barlength = 300
		self.barwidth = 30
		
		self.size = (2 * self.borderwidth + self.barlength , 
					2 * self.borderwidth + self.barwidth)
		
		HUD_Element.__init__(self, hud, position,
				self.size, visible)
	
	def show(self):
		self.clear()
		
		abs = pygame.time.get_ticks() - self.world.player.lastShift
		perc = float(abs) / (CONFIG.PLAYER_SHAPESHIFT_COOLDOWN)
		
		if (perc > 1):
			perc = 1
		
		absbarlength = int(perc * self.barlength)
		pygame.draw.rect(self.surf, (128,255,0),
				pygame.Rect(self.borderwidth,self.borderwidth,
					absbarlength, self.barwidth))
		
		self.surf.blit(self.hud.worldview.images["CoolDownFrame"], (0,0))
		
		HUD_Element.show(self)
	#end class abstract ui element
		

		

class DebugElement(HUD_Element):
	
	
	def __init__(self,
			hud,
			position,
			visible = True):
		
		self.size = (300,100)
		
		
		HUD_Element.__init__(self, hud, position,
				self.size, visible)
	
	def show(self):
		if (not CONFIG.DEBUGMODE): return
		
		self.clear()
		
		#text = str(self.world.player.position)
		text = self.world.player.coll
		label = self.hud.font.render(text, 1, (5,5,5))
		self.surf.blit(label,(0,0))
		
		# call super show
		HUD_Element.show(self)
		
	#end class abstract ui element
		

