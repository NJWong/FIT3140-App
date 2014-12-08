# problems I encountered:
# python does not natively support enums
# python does not support switch statements
# there are a lot of if/elif cascading statements
# could remedy using a dictionary

class robot:
	def __init__(self, x_pos, y_pos, dir):
		self.direction_list = ['N', 'E', 'S', 'W']
		# convention: top left corner is (0, 0)
		# dir is an integer between 0 - 3
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.direction = self.direction_list[dir]

	def get_position(self):
		return (self.x_pos, self.y_pos)

	def get_direction(self):
		return self.direction

	def move_forward(self):
		if self.direction == 'N':
			self.y_pos -= 1
		elif self.direction == 'E':
			self.x_pos =+1
		elif self.direction == 'S':
			self.y_pos += 1
		elif self.direction == 'W':
			self.x_pos -= 1
		else:
			print("robot -> move_forward(): Invalid direction")

	def turn(self, clockwise_flag):
		# TODO include number of turns
		current_dir = self.direction_list.index(self.direction)
		# if clockwise == 1, turn clockwise
		if clockwise_flag == 1:
			new_dir = (current_dir + 1) % 4
		# if clockwise == 0, turn anticlockwise
		elif clockwise_flag == 0:
			new_dir = (current_dir - 1) % 4
		else:
			print("robot -> turn(): invalid clockwise value")
			new_dir = current_dir
		self.direction = self.direction_list[new_dir]

	def update(self):
		pass