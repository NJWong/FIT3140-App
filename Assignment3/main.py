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
			if self.maze.maze[self.robot.posX][self.robot.posY - 1].collide == True:
				return True
		elif self.robot.direction =='E':
			if self.maze.maze[self.robot.posX + 1][self.robot.posY].collide == True:
				return True		
		elif self.robot.direction =='S':
			if self.maze.maze[self.robot.posX][self.robot.posY + 1].collide == True:
				return True	
		elif self.robot.direction =='W':
			if self.maze.maze[self.robot.posX - 1][self.robot.posY].collide == True:
				return True		
		else:
			return False

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

	def move_robot_forward(self):
		if self.robot_can_move_forward():
			#print('main: moving robot forward')
			self.robot.move_forward()

	def robot_can_move_forward(self):
		if self.robot.direction == 'N':
			return self.robot.posY > 0 and self.robot.posY <= self.maze.length
		elif self.robot.direction == 'E':
			return self.robot.posX >= 0 and self.robot.posX < self.maze.length
		elif self.robot.direction == 'S':
			return self.robot.posY >= 0 and self.robot.posY < self.maze.length
		elif self.robot.direction == 'W':
			return self.robot.posX > 0 and self.robot.posX <= self.maze.length

	def show_maze(self):
		self.maze.print_maze()

	def run_program(self, program):
		# move this to the interpreter class

		for expression in program:
			#print('expression start')
			exec(self.interpreter.function_dict[expression])
			#print('expression end')

if __name__ == '__main__':
	my_robot = Robot(0,0,0) # a robot at (0,0) facing East
	my_maze = Maze()
	main = Main(my_robot, my_maze)
	#main.show_maze()
	print(main.robot.posX)
	print(main.robot.posY)
	program = ['m', 't 0 1']
	main.run_program(program)
	print(main.robot.posX)
	print(main.robot.posY)

	# this is my comment
