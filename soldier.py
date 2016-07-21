import pygame, sys
from pygame.locals import *
from gameconst import *

class Soldier:
	def __init__(self, s_type, col, row):
		self.hp = 10
		self.col = col
		self.row = row

class SoldierManager:
	def __init__(self):
		self.soldiers = [[None for j in range(COLS)] for i in range(ROWS)]

	def add_soldier(self, col, row, s_type):
		if self.soldiers[col][row] == None:
			self.soldiers[col][row] = Soldier(s_type, col, row) 
			return True
		return False

	def remove_soldier_by_coor(self, col, row):
		if self.soldiers[col][row] is not None:
			self.soldiers[col][row] = None
		
	def draw(self, map_manager):
		for i in range(ROWS):
			for j in range(COLS):
				if self.soldiers[i][j] is not None:
					map_manager.draw_soldier(self.soldiers[i][j])
