import unittest
from robot import *

# A robot at the top left corner facing North
class robot_moveforward_one(unittest.TestCase):

	def setUp(self):
		self.test_robot = Robot(0,0,0)

	def testOne(self):
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 0 and self.test_robot.posY == -1)

# A robot at the top left corner facing East
class robot_moveforward_two(unittest.TestCase):

	def setUp(self):
		self.test_robot = Robot(0,0,1)

	def testTwo(self):
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 1 and self.test_robot.posY == 0)

# A robot at the top left corner facing South
class robot_moveforward_three(unittest.TestCase):

	def setUp(self):
		self.test_robot = Robot(0,0,2)

	def testTwo(self):
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 0 and self.test_robot.posY == 1)

# A robot at the top left corner facing West
class robot_moveforward_four(unittest.TestCase):

	def setUp(self):
		self.test_robot = Robot(0,0,3)

	def testTwo(self):
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == -1 and self.test_robot.posY == 0)


def main():
	unittest.main()

if __name__ == '__main__':
	main()