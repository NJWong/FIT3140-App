# Import Kivy functionality
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button

class NaviProgram(BoxLayout):
	'''
	The application area that shows the user's program.
	Defines the structure of the program as a ListProperty.
	'''
	program = ListProperty([])

	def add_statement(self, statement):
		'''
		Function that takes a statement and adds it to the program ListProperty.
		Also adds a Button widget to show the statement exists in the NaviProgram area.
		'''
		self.program.append(statement)
		self.add_widget(Button(text=statement))
		#print(self.program)