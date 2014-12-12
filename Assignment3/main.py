from robot import *
from interpreter import *
from maze import *

class Main:
	def __init__(self, robot, maze):
		self.robot = robot
		self.maze = maze
		self.interpreter = Interpreter()

	def detect_wall(self):
		"""
		Identify the tile which the robot is facing currently is a wall or not,
		if it is a wall, then return True; if not, return False
		"""
		if self.robot.direction=='N':
			if self.maze.maze[self.robot.posY - 1][self.robot.posX].collide == True:
				return True
		elif self.robot.direction =='E':
			if self.maze.maze[self.robot.posY][self.robot.posX + 1].collide == True:
				return True		
		elif self.robot.direction =='S':
			if self.maze.maze[self.robot.posY + 1][self.robot.posX].collide == True:
				return True	
		elif self.robot.direction =='W':
			if self.maze.maze[self.robot.posY][self.robot.posX - 1].collide == True:
				return True
		return False

	def distance_to_wall(self):
		"""
		Return the distance from the robot position to the wall which the robot is currently facing
		"""
		distance = -1
		maze = self.maze.maze 
		x=self.robot.posX
		y=self.robot.posY
		while maze[y][x].collide == False:
			if self.robot.direction=='N':
				y -= 1
			elif self.robot.direction=='E':
				x += 1
			elif self.robot.direction=='S':
				y += 1
			elif self.robot.direction=='W':
				x -= 1
			distance += 1
		return distance

	def detect_win(self):
		"""
		Identify the robot is currently standing on the Goal tile or not,
		if yes, return True (probably later, when detect True, it will call sth to end the app); 
		if not, return False
		"""
		if self.maze.maze[self.robot.posX][self.robot.posY].win == True:
			return True
		else:
			return False

	def set_temp_maze(self):
		"""
		Create a temp maze for function search to use
		in order not to affect the original maze.
		"""
		temp_maze = [[0 for x in range(self.maze.length)] for x in range(self.maze.length)]

		for row in range(self.maze.length):
			for column in range(self.maze.length):
				temp_maze[row][column] = self.maze.maze[row][column]
		return temp_maze
		
	def distance_to_goal(self):
		"""
		call function search(x,y) to use recursive way to solve the maze;
		return the distance from robot position to goal.
		Note: the goal self.collide is False, so only when step on it,
		the function can detect the goal,
		thus it is a bit different from function distance_to_wall
		"""
		self.dist = 0
		self.temp_maze = self.set_temp_maze()
		self.search(self.robot.posX,self.robot.posY)
		return self.dist

	def search(self,x,y):
		"""
		Called by distance_to_goal().
		"""
		if self.temp_maze[y][x].desc==' G ':
			return True
		elif self.temp_maze[y][x].desc==' # ':
			return False
		elif self.temp_maze[y][x].desc==' V ':	#the tile has been visited
			return False

		self.temp_maze[y][x].desc = ' V '

<<<<<<< HEAD
		if (x<self.maze.length-1 and self.search(x+1,y)) or (y>0 and self.search(x,y-1)) or (x>0 and self.search(x-1,y))or (y<self.maze.length-1 and self.search(x,y+1)):
			self.dist += 1
=======
		if x<self.maze.length-1 and search(x+1,y) or (y>0 and search(x,y-1)) or (x>0 and search(x-1,y)) or (y<self.maze.length-1 and search(x,y+1)):
>>>>>>> basic layout of application complete. skeleton classes for app completed in navibot.py.
			return True

		return False


	def move_robot_forward(self):
		if self.robot_can_move_forward():
			#print('main: moving robot forward')
			self.robot.move_forward()
			if self.detect_win():
				pass

	def robot_can_move_forward(self):
		# TODO: can edit this to minimise checking 
		if self.robot.direction == 'N':
			return self.robot.posY > 0 and self.robot.posY <= self.maze.length and not self.detect_wall()
		elif self.robot.direction == 'E':
			return self.robot.posX >= 0 and self.robot.posX < self.maze.length and not self.detect_wall()
		elif self.robot.direction == 'S':
			return self.robot.posY >= 0 and self.robot.posY < self.maze.length and not self.detect_wall()
		elif self.robot.direction == 'W':
			return self.robot.posX > 0 and self.robot.posX <= self.maze.length and not self.detect_wall()

	def show_maze(self):
		self.maze.print_maze()

	def run_program(self, program):
		# move this to the interpreter class maybe?
		for expression in program:
			#print('expression start')
			try:
				exec(self.interpreter.function_dict[expression])
			except ValueError:
				return False
			#print('expression end')
		return True

if __name__ == '__main__':
	pass
	#my_robot = Robot(0,0,0) # a robot at (0,0) facing East
	#my_maze = Maze()
	#main = Main(my_robot, my_maze)
	#main.show_maze()
	#print(main.robot.posX)
	#print(main.robot.posY)
	#program = ['m', 't 0 1']
	#main.run_program(program)
	#print(main.robot.posX)
	#print(main.robot.posY)

	# this is my comment
