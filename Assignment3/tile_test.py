from clear import Clear 
from wall import Wall 
from goal import Goal 
import unittest

class create_clear(unittest.TestCase):
	def setUp(self):
		self.test_clear = Clear(0,0)

	def testOne(self):	
		self.assertTrue(self.test_clear.desc==' _ ')


class create_wall(unittest.TestCase):
	def setUp(self):
		self.test_wall = Wall(1,1)

	def testTwo(self):	
		self.assertTrue(self.test_wall.desc==' # ')


class create_goal(unittest.TestCase):
	def setUp(self):
		self.test_goal = Goal(2,2)

	def testThree(self):	
		self.assertTrue(self.test_goal.desc==' G ')


def main():
	unittest.main()


if __name__ =="__main__":
	main()