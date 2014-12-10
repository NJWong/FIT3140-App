import unittest
from main import *
from robot import *
from maze import *

# testing detect_wall


# testing detect_win


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
		print(self.test_main.robot.direction)
		print(self.test_main.robot.posX)
		print(self.test_main.robot.posY)

		self.test_main.move_robot_forward()

		print(self.test_main.robot.direction)
		print(self.test_main.robot.posX)
		print(self.test_main.robot.posY)
		self.assertTrue(
			self.test_main.robot.posX == 1
			and self.test_main.robot.posY == 0
			and self.test_main.robot.direction == 'E')

	# change direction of robot to South and move forward
	# should not change position or direction since it is a wall
	def testThree(self):
		self.test_main.robot.direction = 'S' # hard coded since we have not implemented turn yet
		
		#print(self.test_main.robot.direction)
		#print(self.test_main.robot.posX)
		#print(self.test_main.robot.posY)

		self.test_main.move_robot_forward()

		#print(self.test_main.robot.direction)
		#print(self.test_main.robot.posX)
		#print(self.test_main.robot.posY)

		self.assertTrue(
			self.test_main.robot.posX == 0
			and self.test_main.robot.posY == 0
			and self.test_main.robot.direction == 'S')

# testing robot_can_move_forward


# testing run_program


def main():
	unittest.main()

if __name__ == '__main__':
	main()