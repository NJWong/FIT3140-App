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
		self.assertTrue(self.test_robot.posX == 2 and self.test_robot.posY == 1 and self.test_robot.direction == 'N')

	# testing the robot facing East
	def testTwo(self):
		self.test_robot.direction = 'E' # hard coding since we done turning yet
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 3 and self.test_robot.posY == 2 and self.test_robot.direction == 'E')

	# testing the robot facing South
	def testThree(self):
		self.test_robot.direction = 'S' # hard coding since we done turning yet
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 2 and self.test_robot.posY == 3 and self.test_robot.direction == 'S')

	# testing the robot facing West
	def testFour(self):
		self.test_robot.direction = 'W' # hard coding since we done turning yet
		self.test_robot.move_forward()
		self.assertTrue(self.test_robot.posX == 1 and self.test_robot.posY == 2 and self.test_robot.direction == 'W')


class robot_turn(unittest.TestCase):

	def setUp(self):
		self.test_robot = Robot(2,2,0)

	# turn the robot anticlockwise once
	def testOne(self):
		self.test_robot.turn(0, 1)
		self.assertTrue(self.test_robot.direction == 'W')

	# turn the robot anticlockwise two times
	def testTwo(self):
		self.test_robot.turn(0, 2)
		self.assertTrue(self.test_robot.direction == 'S')

	# turn the robot anticlockwise three times
	def testThree(self):
		self.test_robot.turn(0, 3)
		self.assertTrue(self.test_robot.direction == 'E')

	# turn the robot anticlockwise four times
	def testFour(self):
		self.test_robot.turn(0, 4)
		self.assertTrue(self.test_robot.direction == 'N')

	# turn the robot clockwise once
	def testOne(self):
		self.test_robot.turn(1, 1)
		self.assertTrue(self.test_robot.direction == 'E')

	# turn the robot clockwise two times
	def testTwo(self):
		self.test_robot.turn(1, 2)
		self.assertTrue(self.test_robot.direction == 'S')

	# turn the robot clockwise three times
	def testThree(self):
		self.test_robot.turn(1, 3)
		self.assertTrue(self.test_robot.direction == 'W')

	# turn the robot clockwise four times
	def testFour(self):
		self.test_robot.turn(1, 4)
		self.assertTrue(self.test_robot.direction == 'N')

# integration testing
class robot_moveforward_and_turn(unittest.TestCase):
	pass

def main():
	unittest.main()

if __name__ == '__main__':
	main()
