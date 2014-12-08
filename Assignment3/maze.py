#from clear import Clear 
#from goal import Goal 
#from wall import Wall 

class Maze:
	def __init__(self):
		self.length = 5
		self.maze = self.generate_maze()
		#self.print_maze()

	def generate_maze(self):
		# ' # ' represents a wall
		# ' R ' represents the robot
		# ' _ ' represents a clear
		# ' _ ' represents the goal
		maze = [[' # ' for x in range(self.length)] for x in range(self.length)]

		maze[0][0] = ' R '
		maze[0][1] = ' _ '
		maze[0][2] = ' _ '
		maze[1][2] = ' _ '
		maze[2][2] = ' _ '
		maze[3][2] = ' _ '
		maze[3][3] = ' G '


		return maze

	def print_maze(self):
		for item in self.maze:
			print item



if __name__=="__main__":
	m = Maze()
