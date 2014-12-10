import unittest
from main import *
from robot import *
from maze import *


# testing detect_wall
class test_detect_wall_north(unittest.TestCase):
	"""
	Test when a wall is to the north of the robot 
	"""
	def setUp(self):
		self.test_robot = Robot(3,3,0)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testOne(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_east(unittest.TestCase):
	"""
	Test when a wall is to the east of the robot 
	"""
	def setUp(self):
		self.test_robot = Robot(2,2,1)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testTwo(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_south(unittest.TestCase):
	"""
	Test when a wall is to the south of the robot 
	"""
	def setUp(self):
		self.test_robot = Robot(0,0,2)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testThree(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_west(unittest.TestCase):
	"""
	Test when a wall is to the west of the robot 
	"""
	def setUp(self):
		self.test_robot = Robot(2,2,3)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testFour(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_none(unittest.TestCase):
	"""
	Test when there is no wall around the robot 
	"""
	def setUp(self):
		self.test_robot = Robot(0,0,1)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testFive(self):
		self.assertTrue(self.test_main.detect_wall()==False)

# testing detect_win
class test_detect_win1(unittest.TestCase):
	"""
	Test when the robot reaches the Goal tile
	"""
	def setUp(self):
		self.test_robot = Robot(3,3,0)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testOne(self):
		self.assertTrue(self.test_main.detect_win()==True)

class test_detect_win2(unittest.TestCase):
	"""
	Test when the robot has not reaches the Goal tile 
	"""
	def setUp(self):
		self.test_robot = Robot(0,0,0)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testTwo(self):
		self.assertTrue(self.test_main.detect_win()==False)


# testing move_robot_forward
class move_robot_forward(unittest.TestCase):

	# NOTE: statically created maze might break this test class if changed to
	# dynamically generated maze.

	def setUp(self):
		test_robot = Robot(0,0,0) # initialise a robot at (0,0) facing north
		test_maze = Maze() # might need to define size later

		self.test_main = Main(test_robot, test_maze)


	# try to move the robot forward - should not change position or direction
	def testOne(self):
		self.test_main.move_robot_forward()
		self.assertTrue(
			self.test_main.robot.posX == 0
			and self.test_main.robot.posY == 0
			and self.test_main.robot.direction == 'N')

	# change direction of robot to East and move forward
	def testTwo(self):
		self.test_main.robot.direction = 'E' # hard coded since we have not implemented turn yet
		self.test_main.move_robot_forward()
		self.assertTrue(
			self.test_main.robot.posX == 1
			and self.test_main.robot.posY == 0
			and self.test_main.robot.direction == 'E')

	# change direction of robot to South and move forward
	# should not change position or direction since it is a wall
	def testThree(self):
		self.test_main.robot.direction = 'S' # hard coded since we have not implemented turn yet
		self.test_main.move_robot_forward()
		self.assertTrue(
			self.test_main.robot.posX == 0
			and self.test_main.robot.posY == 0
			and self.test_main.robot.direction == 'S')

	# change direction to West and attempt to move forward
	# should not change position or direction since it is the edge of the maze
	def testFour(self):
		self.test_main.robot.direction = 'W' # hard coded since we have not implemented turn yet
		self.test_main.move_robot_forward()
		self.assertTrue(
			self.test_main.robot.posX == 0
			and self.test_main.robot.posY == 0
			and self.test_main.robot.direction == 'W')


# testing robot_can_move_forward


# testing run_program


def main():
	unittest.main()

if __name__ == '__main__':
	main()