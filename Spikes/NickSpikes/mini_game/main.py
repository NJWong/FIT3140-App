from robot import *
from maze import *

if __name__ == '__main__':
	my_robot = robot(0,0,2)
	print(my_robot.get_position()[0])
	print(my_robot.get_position()[1])
	print(my_robot.get_direction())
	my_maze = maze(5)
	my_maze.print_maze()