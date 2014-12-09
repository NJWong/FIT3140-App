from tile import Tile 

class Goal(Tile):
	def __init__(self,posX,posY):
		Tile.__init__(self,posX,posY)
		self.collide = True
		self.win = True
		self.desc = ' G '