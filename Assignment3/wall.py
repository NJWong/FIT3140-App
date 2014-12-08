from tile import Tile 

class Wall(Tile):
	def __init__(self,posX,posY):
		self.posX = posX
		self.posY = posY
		self.collide = True
		self.win = False
		self.desc = ' # '