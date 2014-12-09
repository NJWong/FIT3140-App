class Robot:
	def __init__(self, posX, posY, direct):
		self.direction_list = ['N', 'E', 'S', 'W']
		self.posX = posX
		self.posY = posY
		self.direction = self.direction_list[direct]

	def move_forward(self):
		#print('robot: moving forward')
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

	def turn(self, clockwise_flag, n):
		# TODO: could optimise the assignments and checking here
		for i in range(n):
			current_dir = self.direction_list.index(self.direction)
			# if clockwise == 1, turn clockwise
			if clockwise_flag == 1:
				new_dir = (current_dir + 1) % 4
			# if clockwise == 0, turn anticlockwise
			elif clockwise_flag == 0:
				new_dir = (current_dir - 1) % 4
			else:
				print("robot -> turn(): invalid clockwise_flag value")
				new_dir = current_dir

			self.direction = self.direction_list[new_dir]