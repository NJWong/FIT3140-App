from robot import *
from interpreter import *
from maze import *

class Main:
	def __init__(self, robot, maze):
		self.robot = robot
		self.maze = maze
		self.interpreter = Interpreter()

	def move_robot_forward(self):
		print('main: moving robot forward')
		self.robot.move_forward()

	def show_maze(self):
		self.maze.print_maze()

	def run_program(self, program):
		# move this to the interpreter class
		for expression in program:
			#print('expression start')
			if expression == 'm':
				self.move_robot_forward()
			#print('expression end')

if __name__ == '__main__':
	my_robot = Robot(0,0,1) # a robot at (0,0) facing East
	my_maze = Maze()
	main = Main(my_robot, my_maze)
	#main.show_maze()
	print(main.robot.posX)
	print(main.robot.posY)

	program = ['m', 'm']
	main.run_program(program)
	print(main.robot.posX)
	print(main.robot.posY)