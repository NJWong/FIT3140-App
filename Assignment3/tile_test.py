from clear import Clear 
from wall import Wall 
from goal import Goal 
import unittest

class create_clear(unittest.Testcase):
	def setUp(self):
		self.test_clear = Clear(0,0)

	def testOne(self):	
		self.assertTrue(self.test_clear.desc)	
if __name__ =="__main__":
	tile_test()