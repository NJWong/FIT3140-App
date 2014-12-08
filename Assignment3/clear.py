from tile import Tile 

class Clear(Tile):
	def __init__(self,posX,posY):
		self.posX = posX
		self.posY = posY
		self.collide = False
		self.win = False
		self.desc = ' _ '