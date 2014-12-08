class maze:
	def __init__(self, size):
		self.size = size
		maze_row = [0]*self.size
		self.maze = [maze_row]*self.size

	def print_maze(self):
		for line in self.maze:
			print(line)

	def insert_robot(self):
		pass