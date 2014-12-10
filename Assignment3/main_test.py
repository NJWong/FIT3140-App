import unittest
from main import *

# testing detect_wall
class test_detect_wall_north(unittest.TestCase):
	def setUp(self):
		self.test_robot = Robot(3,3,0)
		self.test_maze = Maze()
		self.test_main = Main(self.test_robot, self.test_maze)

	def testOne(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_east(unittest.TestCase):
	def setUp(self):
		self.test_robot = robot.Robot(2,2,1)
		self.test_maze = maze.Maze()
		self.test_main = main.Main(self.test_robot, self.test_maze)

	def testTwo(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_south(unittest.TestCase):
	def setUp(self):
		self.test_robot = robot.Robot(0,0,2)
		self.test_maze = maze.Maze()
		self.test_main = main.Main(self.test_robot, self.test_maze)

	def testThree(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_west(unittest.TestCase):
	def setUp(self):
		self.test_robot = robot.Robot(2,2,3)
		self.test_maze = maze.Maze()
		self.test_main = main.Main(self.test_robot, self.test_maze)

	def testFour(self):
		self.assertTrue(self.test_main.detect_wall()==True)

class test_detect_wall_none(unittest.TestCase):
	def setUp(self):
		self.test_robot = robot.Robot(0,0,1)
		self.test_maze = maze.Maze()
		self.test_main = main.Main(self.test_robot, self.test_maze)

	def testFive(self):
		self.assertTrue(self.test_main.detect_wall()==False)

# testing detect_win
class test_detect_win1(unittest.TestCase):
	def setUp(self):
		self.test_robot = robot.Robot(3,3,0)
		self.test_maze = maze.Maze()
		self.test_main = main.Main(self.test_robot, self.test_maze)

	def testOne(self):
		self.assertTrue(self.test_main.detect_win()==True)

class test_detect_win2(unittest.TestCase):
	def setUp(self):
		self.test_robot = robot.Robot(0,0,0)
		self.test_maze = maze.Maze()
		self.test_main = main.Main(self.test_robot, self.test_maze)

	def testTwo(self):
		self.assertTrue(self.test_main.detect_win()==False)

"""
# testing move_robot_forward
class move_robot_forward(unittest.TestCase):

	# NOTE: statically created maze might break this test class if changed to
	# dynamically generated maze.

	def setUp(self):
		test_robot = Robot()
		test_maze = Maze()

		test_main = Main(test_robot, test_maze, test_interpreter)

	def testOne(self):"""


# testing robot_can_move_forward


# testing run_program


def main():
	unittest.main()

if __name__ == '__main__':
	main()