from tile import Tile 

class Wall(Tile):
	"""
	Inheritance from Tile class;
	to restrict the move of the robot
	"""
	def __init__(self,posX,posY):
		Tile.__init__(self,posX,posY)
		self.collide = True
		self.win = False
		self.desc = ' # '


