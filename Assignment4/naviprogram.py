# Import Kivy functionality
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, DictProperty
from kivy.uix.button import Button

class NaviProgram(BoxLayout):
	'''
	The application area that shows the user's program.
	Defines the structure of the program as a ListProperty.
	'''
	program = ListProperty([])
	variable_dict = DictProperty({})
	function_dict = DictProperty({})

	def print_var_dict(self):
		var_dict = ''
		for variable in self.variable_dict:
			var_dict += '%s : %r\n' % (variable, self.variable_dict[variable])
		return var_dict

	def add_statement(self, statement):
		'''
		Function that takes a statement and adds it to the program ListProperty.
		Also adds a Button widget to show the statement exists in the NaviProgram area.
		'''
		# TODO: tidy this abomination up...
		print(self.program)
		if statement.split()[0] != 'Comment:':
			self.program.append(statement)
		if statement.split(',')[0] == 'SET_L':
			# TODO type validation
			self.variable_dict[statement.split(',')[1]] = statement.split(',')[2]
		if statement.split(',')[0] == 'BUILD_LIST':
			# TODO type validation
			self.variable_dict[statement.split(',')[1]] = str(statement.split(',')[2:])
		if len(self.program) >= 2:
			if self.program[-2].split(',')[0] == 'SET_TO' and len(self.program[-2].split(',')) != 3:
				self.merge_set_to()
		if statement == 'ENDIF':
			self.merge_if_statement()
		if statement == 'ENDCOND':
			self.merge_conditional()
		if statement == 'ENDFUNCTION':
			self.merge_function()
		self.add_widget(Button(text=statement))

		print(self.program)
		#print(self.variable_dict)

	def merge_set_to(self):
		# guarenteed to be the last two elements
		# merge into form
		# SET_TO,variable,result
		set_to = 'SET_TO,%s,%s' % (self.program[-2].split(',')[1], (self.program[-1]))
		self.program = self.program[:-2]
		self.program.append(set_to)

	def merge_function(self):
		# merge into form
		# start:
		# 'FUNCTION', 'f1 n', 'MOVE', 'ENDFUNCTION'
		# end:
		# 'FUNCTION (name) (args) (statement),(statement) ENDFUNCTION'

		start_funct_index = self.program.index('FUNCTION')
		end_funct_index = self.program.index('ENDFUNCTION')

		temp_funct = self.program[start_funct_index:]
		self.program = self.program[:start_funct_index]
		funct = ''
		for s in temp_funct:
			if s == 'FUNCTION':
				funct += '%s ' % s
			elif s == 'ENDFUNCTION':
				# remove the last comma
				funct = funct[:-1]
				funct += ' %s' % s
			elif len(s.split()) > 1:
				funct += '%s ' % s
			else:
				funct += '%s,' % s
		self.program.append(funct)

	def merge_conditional(self):
		# merge into form:
		# "COND (comparator)(boolean)(comparator) ENDCOND"
		start_cond_index = self.program.index('COND')
		end_cond_index = self.program.index('ENDCOND')

		temp_cond = self.program[start_cond_index:]
		self.program = self.program[:start_cond_index]
		cond = ''
		for s in temp_cond:
			if s == 'COND':
				cond += 'COND '
			elif s == 'ENDCOND':
				cond += ' ENDCOND'
			else:
				cond += '%s' % s
		self.program.append(cond)

	def merge_if_statement(self):
		# merge into the form:
		# IF,(condition),statement,statement,ENDIF
		start_if_index = self.program.index('IF')
		end_if_index = self.program.index('ENDIF')
		temp_if = self.program[start_if_index:]
		self.program = self.program[:start_if_index]
		if_statement = ''
		for s in temp_if:
			if_statement += '%s,' % s
		if_statement = if_statement[:-1] # remove the last comma
		self.program.append(if_statement)

	def reset(self):
		self.program = []
		self.variable_dict = {}
		self.clear_widgets()
