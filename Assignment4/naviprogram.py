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
	program = ListProperty([]) # The NaviProgram taken from the blocks as a list. This is what the interpreter interprets
	variable_dict = DictProperty({}) # The variables defined by the program stored in a dictionary
	function_dict = DictProperty({}) # The functions defined by the program stored in a dictionary

	def add_statement(self, statement):
		'''
		Function that takes a statement and adds it to the program ListProperty.
		Also adds a Button widget to show the statement exists in the NaviProgram area.
		'''
		# TODO: tidy this abomination up...
		add = True
		if statement.split()[0] != 'Comment:':
			if statement.split()[0] == 'TURN_A' or statement.split()[0] == 'TURN_C':
				try:
					int(statement.split()[1])
					self.program.append(statement)
				except:
					try:
						self.variable_dict[statement.split()[1]]
						self.program.append(statement)
					except KeyError:
						print('Not found in variable dictionary')
						add = False
			else:
				self.program.append(statement)

		if statement.split(',')[0] == 'HEAD_LIST':
			self.eval_head_list()
		if statement.split(',')[0] == 'TAIL_LIST':
			self.eval_tail_list()
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

		if add:
			self.add_widget(Button(text=statement))

		print('Program: ',self.program)
		print(self.variable_dict)

	def eval_head_list(self):
		'''
		Function that is called to evaluate a head function call
		on a list. Returns the head of the list.
		Should be used in conjunction with SET_TO in order to be useful
		'''
		tmp_head = self.program[-1].split(',')
		head_statement = '%s[0]' % tmp_head[1]
		self.program = self.program[:-1]
		self.program.append(head_statement)

	def eval_tail_list(self):
		'''
		Function that is called to evaluate a tail function call
		on a list. Returns the tail of the list.
		Should be used in conjunction with SET_TO in order to be useful
		'''
		tmp_tail = self.program[-1].split(',')
		tail_statement = '%s[1:]' % tmp_tail[1]
		self.program = self.program[:-1]
		self.program.append(tail_statement)

	def merge_set_to(self):
		'''
		Function that is called when a SET_TO function is used
		The SET_TO block and the result block is guarenteed to be the last two entries in self.program
		so we can edit them directly.
		This function appends a merged SET_TO statement that can be interpreted by the interpreter in
		the same say that SET_L is interpreted.
		'''
		set_to = 'SET_TO,%s,%s' % (self.program[-2].split(',')[1], (self.program[-1]))
		self.variable_dict[self.program[-2].split(',')[1]] =  self.program[-1]# add to variable dictionary
		self.program = self.program[:-2]
		self.program.append(set_to) # append to the program


	def merge_function(self):
		'''
		Function that is called when an ENDFUNCTION block is added
		IMPORTANT: this is not completed yet
		'''

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
		'''
		Function that is called when an ENDCOND is detected
		Takes the fragmented boolean expression in between COND
		and ENDCOND and merges it into a single conditional statement
		that can be interpreted by the interpreter
		'''
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
			elif s == 'not':
				cond += ' %s' % s
			else:
				cond += '%s' % s
		self.program.append(cond)

	def merge_if_statement(self):
		'''
		Function that is called when an ENDIF is detected
		Takes the fragmented if-statement in between IF and
		ENDIF and merges it into a single if-statement that can
		be interpreted by the interpreter.
		'''
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
