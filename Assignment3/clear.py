#!/usr/bin/env python -B
from tile import Tile 

class Clear(Tile):
	def __init__(self,posX,posY):
		Tile.__init__(self,posX,posY)
		self.collide = False
		self.win = False
		self.desc = ' _ '
