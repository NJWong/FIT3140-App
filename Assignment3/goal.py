from tile import Tile 

class Goal(Tile):
	"""
	Inheritance from the Tile class
	The goal for the robot to aim at
	"""
	def __init__(self,posX,posY):
		Tile.__init__(self,posX,posY)
		self.collide = False
		self.win = True
		self.desc = ' G '

