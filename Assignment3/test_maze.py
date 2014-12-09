from maze import Maze 
import unittest

class test_maze(unittest.TestCase):
	def setUp(self):
		self.test_maze = Maze()

	def testOne(self):
		for row in self.test_maze.maze:
			for column in row:
				self.assertTrue(column.desc==' _ ' or column.desc==' G ' or column.desc==' # ')


def main():
	unittest.main()


if __name__ == '__main__':
	main()
