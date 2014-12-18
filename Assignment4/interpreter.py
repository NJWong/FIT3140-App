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
		self.interpreter_dict = {
		'SET':'self.set_variable(%s)',
		'FUNCTION':'self.define_function(%s)',
		'CALL':'self.call_function(%s)'
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

	def set_variable(self, split_statement):
		print(split_statement)

	def define_function(self, split_statement):
		print(split_statement)

	def call_function(self, split_statement):
		print(split_statement)

	def run(self, program):
		python_code = ''

		for statement in program:
			split_statement = statement.split()

			exec(self.interpreter_dict[split_statement[0]] % split_statement)

if __name__ == '__main__':
	i = Interpreter()
	program = ["SET number 3", "FUNCTION hello n if,(n>1),print('hello'),endif,print('world')", "CALL hello number"]
	i.run(program)



