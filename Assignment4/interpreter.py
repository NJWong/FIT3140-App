class Interpreter:
	'''
	The interpreter class that defines the functions and algorithms to read,
	parse, and evaluate a program.
	'''
	# Basic data types defined in terms of python data types
	Integer = int
	Boolean = bool
	List = list

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


if __name__ == '__main__':
	#testOne()
	testTwo()




