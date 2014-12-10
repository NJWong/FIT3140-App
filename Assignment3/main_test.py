import unittest
import main

# testing detect_wall


# testing detect_win


# testing move_robot_forward
class move_robot_forward(unittest.TestCase):

	# NOTE: statically created maze might break this test class if changed to
	# dynamically generated maze.

	def setUp(self):
		test_robot = Robot()
		test_maze = Maze()

		test_main = Main(test_robot, test_maze, test_interpreter)

	def testOne(self):


# testing robot_can_move_forward


# testing run_program


def main():
	unittest.main()

if __name__ == '__main__':
	main()