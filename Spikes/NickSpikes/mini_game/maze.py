class maze:
	def __init__(self, size):
		#maze_row = ['-']*self.size
		#self.maze = [maze_row]*self.size
		self.maze = [['-' for x in range(size)] for x in range(size)]

	def print_maze(self):
		for line in self.maze:
			print(line)

	def update(self):
		pass