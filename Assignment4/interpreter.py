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
		'TURN_A':'turn_anticlockwise(%s)',
		'TURN_C': 'turn_clockwise(%s)',
		'DISTANCE_W': 'distance_to_wall()',
		'DISTANCE_G': 'distance_to_goal()'
		}

		#'SET %s TO %s' % (name,value): 'set_var(%s, %s)' % (name, value) #not sure...
		self.operator_dict = {
		'add':op.add, 'sub':op.sub, 'mult':op.mul, 'div':op.div, 'mod':op.mod
		}
		self.boolean_dict = {
		'==':op.eq, '<':op.lt, '>':op.gt
		}
		# functions that the interpreter uses definitions, initialisations, or function calls
		self.interpreter_dict = {
		'SET':'self.set_variable(%s)',
		'FUNCTION':'self.define_function(%s)',
		'CALL':'self.call_function(%s)',
		'IF':'self.create_if_statement(%s)',
		'LIST':'self.create_list(%s)'
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
		split_statement = statement.split()
		try:
			if split_statement[0] == 'TURN_A':
				return 'self.navimaze.'+self.function_dict[split_statement[0]] % split_statement[1]
			elif split_statement[0] == 'TURN_C':
				return 'self.navimaze.'+self.function_dict[split_statement[0]] % split_statement[1]
			else:
				return 'self.navimaze.'+self.function_dict[statement]
		except KeyError:
			print('Statement not recognised: passing')
			return 'pass'

	def set_variable(self, split_statement):
		#print(split_statement)
		set_statement = '%s = %s\n' % (split_statement[1], split_statement[2])
		return set_statement

	def define_function(self, split_statement):
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
		for s in s_list:
			if s == 'IF':
				function_statement += '%sif ' % ('\t'*indents)
				indents += 1
			elif s[0] == '(':
				function_statement += '%s:\n' % (s)
			elif s == 'ENDIF':
				indents -= 1
			else:
				function_statement += '%s%s\n' % (('\t'*indents), s)

		return function_statement

	def call_function(self, split_statement):
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
		return call_statement

	def create_if_statement(self, split_statement):
		if_statement = 'if '
		for s in split_statement[1].split():
			if s != 'COND' and s != 'ENDCOND':
				if_statement += s
		if_statement += ':\n'
		for s in split_statement[2:]:
			if s != 'ENDIF':
				if_statement += ('\tself.navimaze.%s\n' % self.function_dict[s])
			#print(if_statement)
		return if_statement

	def call_inbuilt_function(self, split_statement):
		pass

	def interpret(self, program):
		python_code = ''

		for statement in program:
			split_statement = statement.split()
			if split_statement[0] in self.function_dict:
				try:
					if split_statement[0] == 'TURN_A':
						new_statement = 'self.navimaze.%s\n' % (self.function_dict[split_statement[0]] % split_statement[1])
						python_code += new_statement
					elif split_statement[0] == 'TURN_C':
						new_statement = 'self.navimaze.%s\n' % (self.function_dict[split_statement[0]] % split_statement[1])
						python_code += new_statement
					else:
						new_statement = 'self.navimaze.%s\n' % (self.function_dict[split_statement[0]])
						python_code += new_statement
				except KeyError:
					print('Statement not recognised: passing')
					return 'pass'
			elif statement.split(',')[0] in self.interpreter_dict:
				new_statement = eval(self.interpreter_dict[statement.split(',')[0]] % statement.split(','))
				python_code += new_statement
			else:
				print('found nothing...')

		#print(python_code)
		return python_code

	def run(self, python_code):
		exec(python_code)

if __name__ == '__main__':
	i = Interpreter()
	program = ["SET number 0", "FUNCTION hello n if,(n>1),print('hello'),endif,print('world')", "CALL hello number"]
	i.interpret(program)



