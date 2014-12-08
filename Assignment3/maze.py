from clear import Clear 
from goal import Goal 
from wall import Wall 

class Maze:
	def __init__(self):
		self.length = 5
		self.maze = self.generate_maze()
		self.print_maze()

	def generate_maze(self):
		maze = [[0 for x in range(self.length)] for x in range(self.length)]

		for row in range(self.length):
			for column in range(self.length):
				maze[row][column] = Wall(row,column)

		maze[0][1] = Clear(0,1)
		maze[0][2] = Clear(0,2)
		maze[1][2] = Clear(1,2)
		maze[2][2] = Clear(2,2)
		maze[3][2] = Clear(3,2)
		maze[3][3] = Goal(3,3) 

		return maze

	def print_maze(self):
		# ' # ' represents a wall
		# ' R ' represents the robot
		# ' _ ' represents a clear
		# ' G ' represents the goal
		for row in range(self.length):
			string1 = ''
			for column in range(self.length):
				string1 += self.maze[row][column].desc
			print string1




if __name__=="__main__":
	m = Maze()
