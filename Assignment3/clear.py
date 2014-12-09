from tile import Tile 

class Clear(Tile):
	"""
	Inheritance class from Tile;
	it can be travelled across by the robot, 
	and will not affected the robot
	"""
	def __init__(self,posX,posY):
		Tile.__init__(self,posX,posY)
		self.collide = False
		self.win = False
		self.desc = ' _ '
