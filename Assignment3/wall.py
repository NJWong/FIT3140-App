from tile import Tile 

class Wall(Tile):
	def __init__(self,posX,posY):
		Tile.__init__(self,posX,posY)
		self.collide = True
		self.win = False
		self.desc = ' # '


