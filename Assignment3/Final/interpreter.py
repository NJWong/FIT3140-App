class Interpreter:
	def __init__(self):
		self.running = False
		self.function_dict = {
		'MOVE':'move_robot()',
		'TURN_A':'turn_anticlockwise()',
		'TURN_C': 'turn_clockwise()'
		}

	def create_execution_tree(self, program):
		execution_tree = []
		for statement in program:
			execution_tree.append(self.execute(statement))
		return execution_tree

	def execute(self, statement):
		return 'self.navimaze.'+self.function_dict[statement]