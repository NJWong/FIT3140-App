class Interpreter:
	'''
	The interpreter class that defines the functions and algorithms to read,
	parse, and evaluate a program.
	'''
	# Basic data types defined in terms of python data types
	Integer = int
	Boolean = bool
	List = list

	name = ''
	value = ''

	global name, value

	def __init__(self):
		import math, operator as op
		self.running = False
		# Statements found in NaviProgram.py are mapped to functions to be called in NaviBot.py
		self.function_dict = {
		'MOVE':'move_robot()',
		'TURN_A':'turn_anticlockwise()',
		'TURN_C': 'turn_clockwise()',
		'DISTANCE_W': 'distance_to_wall()',
		'DISTANCE_G': 'distance_to_goal()',
		'DISTANCE_G': 'distance_to_goal()',
		'FUNCTION': 'define_function()'
		}

		#'SET %s TO %s' % (name,value): 'set_var(%s, %s)' % (name, value) #not sure...
		self.operator_dict = {
		'add':op.add, 'sub':op.sub, 'mult':op.mul, 'div':op.div, 'mod':op.mod
		}
		self.boolean_dict = {
		'==':op.eq, '<':op.lt, '>':op.gt
		}

	def create_execution_tree(self, program):
		'''
		A function that takes a program and parses it into an execution tree.
		Note: Simple implementation for the moment - will become more complex as
		more functions are included.
		'''
		execution_tree = []
		for statement in program:
			execution_tree.append(self.execute(statement))
		return execution_tree

	def execute(self, statement):
		'''
		returns the appropriate function to be called inside NaviBot.py
		'''
		try:
			return 'self.navimaze.'+self.function_dict[statement]
		except KeyError:
			print('Statement not recognised: passing')
			return 'pass'

if __name__ == '__main__':
	statement = "DEFINE hello n print('hello'),print('world')"
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
	parsed_arg_string = arg_string.split(',')
	print(parsed_arg_string)

	# parse the statement_string
	parsed_statement_string = statement_string.split(',')
	print(parsed_statement_string)

	# start the function string
	function = "def %s(" % name
	print(function)

	# add the arguments to the function string
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

	print(function)



