# A specification testing file for Interpreter found in interpreter.py
import unittest
from interpreter import *

# Testing basic programming data types
class test_data_types(unittest.TestCase):
	def setUp(self):
		self.test_interpreter = Interpreter()

	# Test Integer type
	def testOne(self):
		self.assertTrue(type(self.test_interpreter.Integer) is type(int))

	# Test Boolean type
	def testTwo(self):
		self.assertTrue(type(self.test_interpreter.Boolean) is type(bool))

	# Test List type
	def testThree(self):
		self.assertTrue(type(self.test_interpreter.List) is type(list))

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

# parsing a statement
def testOne():
	statement = "FUNCTION hello None print('hello'),print('world')"
	print(statement)

	# Parse the statement
	parsed_statement = statement.split()
	print(parsed_statement)

	# Read the parsed statement
	name = parsed_statement[1]
	arg_string = parsed_statement[2]
	statement_string = parsed_statement[3]
	print(name)
	print(arg_string)
	print(statement_string)

	# parse the arg_string
	if arg_string == 'None':
		# there are no args
		parsed_arg_string = []
	else:
		parsed_arg_string = arg_string.split(',')
	
	print(parsed_arg_string)

	# parse the statement_string
	parsed_statement_string = statement_string.split(',')
	print(parsed_statement_string)

	# start the function string
	function = "def %s(" % name
	print(function)

	# add the arguments to the function string
	if arg_string != 'None':
		for arg in parsed_arg_string:
			function += (arg)
			function += (',')
		print(function)
	# remove the last comma
		function = function[:-1]
	print(function)

	# close the arguments and add a new line
	function += '):\n'
	print(function)
	
	# add indentation to the parsed_statement_string
	for s in parsed_statement_string:
		function += '\t'
		function += s
		function += '\n'

	print(function)

	exec(function)
	hello()

def testTwo():
	# a program is a series of statements
	program = ["SET number 3", "FUNCTION hello n if,(n>1),print('hello'),endif,print('world')", "CALL hello number"]

	python_code = ''

	# for each of the statements, convert them to python code
	for statement in program:
		# split the statement up
		split_statement = statement.split()
		#print(split_statement)
		if split_statement[0] == 'SET':
			#print('set')
			set_statement = '%s = %s\n' % (split_statement[1], split_statement[2])
			python_code += set_statement
		elif split_statement[0] == 'FUNCTION':
			#print('function')
			function_statement = 'def %s(' % (split_statement[1])
			# add the args
			arg_list = split_statement[2].split()
			for arg in arg_list:
				function_statement += arg
				function_statement += ','
			function_statement = function_statement[:-1]
			function_statement += '):\n'

			# Add the statements
			s_list = split_statement[3].split(',')
			indents = 1
			print(s_list)
			for s in s_list:
				if s == 'if':
					function_statement += '%sif ' % ('\t'*indents)
					indents += 1
				elif s[0] == '(':
					function_statement += '%s:\n' % (s)
				elif s == 'endif':
					indents -= 1
				else:
					function_statement += '%s%s\n' % (('\t'*indents), s)

			python_code += function_statement
			print(function_statement)
		elif split_statement[0] == 'CALL':
			#print('call')
			call_statement = '%s(' % split_statement[1]
			# add the arguments
			# TODO handle no args
			for arg in split_statement[2:]:
				call_statement += arg
				call_statement += ','
			# remove the last comma
			# TODO handle no args
			call_statement = call_statement[:-1]
			call_statement += ')'
			python_code += call_statement

		#print(python_code)
		exec(python_code)