class Robot:
	def __init__(self, posX, posY, direct):
		direction_list = ['N', 'E', 'S', 'W']
		self.posX = posX
		self.posY = posY
		self.direction = direction_list[direct]

	def move_forward(self):
		print('robot: moving forward')
		if self.direction == 'N':
			self.posY -= 1
		elif self.direction == 'E':
			self.posX += 1
		elif self.direction == 'S':
			self.posY += 1
		elif self.direction == 'W':
			self.posX -= 1
		else:
			print('invalid direction')