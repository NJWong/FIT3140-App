from tile import Tile 

class Goal(Tile):
	def __init__(self,posX,posY):
		self.posX = posX
		self.posY = posY
		self.collide = True
		self.win = True
		self.desc = ' G '