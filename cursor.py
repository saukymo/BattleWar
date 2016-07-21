import pygame, sys
from pygame.locals import *

from gameconst import *

class Cursor:

	def __init__(self, surface):
		self.surface = surface
		self.x = 0
		self.y = 0
		self.visible = True

	def set_position(self, mouse_pos):
		self.x = mouse_pos.x
		self.y = mouse_pos.y

	def set_visible(self, state):
		self.visible = state

	def draw(self):
		if self.visible:
			pygame.draw.circle(self.surface, (0, 0, 170), (self.x, self.y), 5, 1)