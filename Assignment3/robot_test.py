import unittest
from robot import *

# A robot at positon 2, 2
# Since boundary or tile checking is not done in the robot class,
# we are not testing that in this set of unit tests
class robot_moveforward_one(unittest.TestCase):

	# initialise the robot facing North
	def setUp(self):
		self.test_robot = Robot(2,2,0)

	# testing the robot facing North
	def testOne(self):
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 2 and self.test_robot.posY == 1)

	# testing the robot facing East
	def testTwo(self):
		self.test_robot.direction = 'E' # hard coding since we done turning yet
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 3 and self.test_robot.posY == 2)

	# testing the robot facing South
	def testThree(self):
		self.test_robot.direction = 'S' # hard coding since we done turning yet
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 2 and self.test_robot.posY == 3)

	# testing the robot facing West
	def testFour(self):
		self.test_robot.direction = 'W' # hard coding since we done turning yet
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 1 and self.test_robot.posY == 2)

def main():
	unittest.main()

if __name__ == '__main__':
	main()