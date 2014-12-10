# Type definitions
class Interpreter:

	def __init__(self):
		Integer = int
		Boolean = bool
		List = list
		self.function_dict = {
		'm':'self.move_robot_forward()',
		'd_wall':'self.detect_wall()',
		'd_win':'self.detect_win()'
		}

	def tokenize(self, chars):
		return chars.replace('(', ' ( ').replace(')', ' ) ').split()

	def parse(self, program):
		return self.read_from_tokens(self.tokenize(program))

	def read_from_tokens(self, tokens):
		if len(tokens) == 0:
			raise SyntaxError('unexpected EOF while reading')
		token = tokens.pop(0)
		if token == '(':
			L = []
			while tokens[0] != ')':
				L.append(self.read_from_tokens(tokens))
			tokens.pop(0) # remove the ending ')'
			return L
		elif token == ')':
			raise SyntaxError('unexpected')
		else:
			return self.atom(token)

	def atom(self, token):
		try:
			return int(token)
		except ValueError:
			try:
				return bool(token)
			except ValueError:
				try:
					return list(token)
				except ValueError:
					print('Not recognised type')
					return str(token)



