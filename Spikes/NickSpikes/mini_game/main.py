from robot import *
from maze import *

class main:

	def __init__(self, robot, maze):
		self.robot = robot
		self.maze = maze

	def move_robot_forward(self):
		# TODO check for OOB
		self.robot.move_forward()
		self.update_maze()

	def turn_robot(self, clockwise_flag):
		self.robot.turn(clockwise_flag)
		print('New direction: %r' % self.robot.direction)

	def update_maze(self):
		self.maze.maze[self.robot.y_pos][self.robot.x_pos] = 'X'
		self.maze.print_maze()
		print('\n')

if __name__ == '__main__':
	my_robot = robot(0,0,2)
	my_maze = maze(5)
	main = main(my_robot, my_maze)
	main.update_maze()
	main.move_robot_forward()
	main.move_robot_forward()
	main.move_robot_forward()
	main.move_robot_forward()
	main.turn_robot(0)
	main.move_robot_forward()
