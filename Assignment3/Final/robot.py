from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ListProperty

class Robot(Button):
	'''
	A robot entity class that defines the cartesian location of the robot, as well
	as the direction it is facing.
	'''
	posX = NumericProperty(0) # Hard coded for now
	posY = NumericProperty(0) # Hard coded for now
	direction = StringProperty('E') # Hard coded for now
	direction_list = ListProperty(['N', 'E', 'S', 'W'])
	distance_to_wall = NumericProperty(None)

	def move_forward(self):
		'''
		Move the robot forward once based on its current direction
		'''
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
		'''
		Turn the robot n times in a clockwise direction if 'clockwise_flag' = 1,
		else turn it n times anticlockwise.
		'''
		# TODO: could optimise the assignments and checking here
		for i in range(n):
			current_dir = self.direction_list.index(self.direction)
			# if clockwise == 1, turn clockwise
			if clockwise_flag == 1:
				new_dir = (current_dir + 1) % 4 # Essentially using a circular queue to cycle directions
			# if clockwise == 0, turn anticlockwise
			elif clockwise_flag == 0:
				new_dir = (current_dir - 1) % 4
			else:
				print("robot -> turn(): invalid clockwise_flag value")
				new_dir = current_dir

			self.direction = self.direction_list[new_dir]