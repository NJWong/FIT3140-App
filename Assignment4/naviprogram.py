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

	def add_statement(self, statement):
		'''
		Function that takes a statement and adds it to the program ListProperty.
		Also adds a Button widget to show the statement exists in the NaviProgram area.
		'''
		self.program.append(statement)
		if statement.split()[0] == 'SET':
			# TODO type validation
			self.variable_dict[statement.split()[1]] = statement.split()[2]
		if statement.split(',')[0] == 'BUILD_LIST':
			# TODO type validation
			self.variable_dict[statement.split(',')[1]] = str(statement.split(',')[2:])
		if statement == 'ENDIF':
			self.merge_if_statement()
		if statement == 'ENDCOND':
			self.merge_conditional()
		self.add_widget(Button(text=statement))
		#print(self.program)
		#print(self.variable_dict)

	def merge_conditional(self):
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
