# A specification testing file for Interpreter found in interpreter.py
import unittest
from interpreter import *

# Testing basic programming data types
class test_data_types(unittest.TestCase):
	def setUp(self):
		self.test_interpreter = Interpreter()

	# Test Integer type
	def testOne(self):
		pass
		#self.assertTrue(type(self.test_interpreter.Integer) is type(int))

	# Test Boolean type
	def testTwo(self):
		pass

	# Test List type
	def testThree(self):
		pass

# Testing mathematical operations
class test_math_operations(unittest.TestCase):
	def setUp(self):
		self.test_interpreter = Interpreter()
		self.operand1 = 1
		self.operand2 = 5
		self.operand3 = 10
		self.operand4 = 50
		self.operand5 = 100
		# TODO: add non-integer values

	# Test add operator
	def testOne(self):
		self.assertTrue(self.test_interpreter.operator_dict['add'](self.operand1, self.operand1) == 2)
		self.assertTrue(self.test_interpreter.operator_dict['add'](self.operand1, self.operand2) == 6)
		self.assertTrue(self.test_interpreter.operator_dict['add'](self.operand1, self.operand3) == 11)
		self.assertTrue(self.test_interpreter.operator_dict['add'](self.operand1, self.operand4) == 51)
		self.assertTrue(self.test_interpreter.operator_dict['add'](self.operand1, self.operand5) == 101)

	# Test sub operator
	def testTwo(self):
		self.assertTrue(self.test_interpreter.operator_dict['sub'](self.operand1, self.operand1) == 0)
		self.assertTrue(self.test_interpreter.operator_dict['sub'](self.operand2, self.operand1) == 4)
		self.assertTrue(self.test_interpreter.operator_dict['sub'](self.operand3, self.operand1) == 9)
		self.assertTrue(self.test_interpreter.operator_dict['sub'](self.operand4, self.operand1) == 49)
		self.assertTrue(self.test_interpreter.operator_dict['sub'](self.operand5, self.operand1) == 99)

	# Test mult operator
	def testThree(self):
		self.assertTrue(self.test_interpreter.operator_dict['mult'](self.operand1, self.operand1) == 1)
		self.assertTrue(self.test_interpreter.operator_dict['mult'](self.operand1, self.operand2) == 5)
		self.assertTrue(self.test_interpreter.operator_dict['mult'](self.operand1, self.operand3) == 10)
		self.assertTrue(self.test_interpreter.operator_dict['mult'](self.operand1, self.operand4) == 50)
		self.assertTrue(self.test_interpreter.operator_dict['mult'](self.operand1, self.operand5) == 100)

	# Test div operator
	def testFour(self):
		self.assertTrue(self.test_interpreter.operator_dict['div'](self.operand1, self.operand1) == 1)
		self.assertTrue(self.test_interpreter.operator_dict['div'](self.operand1, self.operand2) == 0)
		self.assertTrue(self.test_interpreter.operator_dict['div'](self.operand1, self.operand3) == 0)
		self.assertTrue(self.test_interpreter.operator_dict['div'](self.operand1, self.operand4) == 0)
		self.assertTrue(self.test_interpreter.operator_dict['div'](self.operand1, self.operand5) == 0)

	# Test mod operator
	def testFive(self):
		self.assertTrue(self.test_interpreter.operator_dict['mod'](self.operand1, self.operand1) == 0)
		self.assertTrue(self.test_interpreter.operator_dict['mod'](self.operand1, self.operand2) == 1)
		self.assertTrue(self.test_interpreter.operator_dict['mod'](self.operand1, self.operand3) == 1)
		self.assertTrue(self.test_interpreter.operator_dict['mod'](self.operand1, self.operand4) == 1)
		self.assertTrue(self.test_interpreter.operator_dict['mod'](self.operand1, self.operand5) == 1)

# Testing boolean operations
class test_boolean_operations(unittest.TestCase):

	def setUp(self):
		self.test_interpreter = Interpreter()
		self.operand1 = 1
		self.operand2 = 2
		self.operand3 = 3
		# TODO: add non-integer values

	# Test equality '==' operator
	def testOne(self):
		self.assertTrue(self.test_interpreter.boolean_dict['=='](self.operand1, self.operand1))
		self.assertTrue(not self.test_interpreter.boolean_dict['=='](self.operand1, self.operand2))
		self.assertTrue(not self.test_interpreter.boolean_dict['=='](self.operand1, self.operand3))
		self.assertTrue(self.test_interpreter.boolean_dict['=='](self.operand2, self.operand2))
		self.assertTrue(not self.test_interpreter.boolean_dict['=='](self.operand2, self.operand3))
		self.assertTrue(self.test_interpreter.boolean_dict['=='](self.operand3, self.operand3))

	# Test less than '<' operator
	def testTwo(self):
		self.assertTrue(not self.test_interpreter.boolean_dict['<'](self.operand1, self.operand1))
		self.assertTrue(self.test_interpreter.boolean_dict['<'](self.operand1, self.operand2))
		self.assertTrue(self.test_interpreter.boolean_dict['<'](self.operand1, self.operand3))
		self.assertTrue(not self.test_interpreter.boolean_dict['<'](self.operand2, self.operand2))
		self.assertTrue(self.test_interpreter.boolean_dict['<'](self.operand2, self.operand3))
		self.assertTrue(not self.test_interpreter.boolean_dict['<'](self.operand3, self.operand1))
		self.assertTrue(not self.test_interpreter.boolean_dict['<'](self.operand3, self.operand2))
		self.assertTrue(not self.test_interpreter.boolean_dict['<'](self.operand3, self.operand3))

	# Test greater than '>' operator
	def testThree(self):
		self.assertTrue(not self.test_interpreter.boolean_dict['>'](self.operand1, self.operand1))
		self.assertTrue(not self.test_interpreter.boolean_dict['>'](self.operand1, self.operand2))
		self.assertTrue(not self.test_interpreter.boolean_dict['>'](self.operand1, self.operand3))
		self.assertTrue(self.test_interpreter.boolean_dict['>'](self.operand2, self.operand1))
		self.assertTrue(not self.test_interpreter.boolean_dict['>'](self.operand2, self.operand2))
		self.assertTrue(not self.test_interpreter.boolean_dict['>'](self.operand2, self.operand3))
		self.assertTrue(self.test_interpreter.boolean_dict['>'](self.operand3, self.operand1))
		self.assertTrue(self.test_interpreter.boolean_dict['>'](self.operand3, self.operand2))
		self.assertTrue(not self.test_interpreter.boolean_dict['>'](self.operand3, self.operand3))

def main():
	unittest.main()

if __name__ == '__main__':
	main()