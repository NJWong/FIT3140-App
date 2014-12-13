from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button

from interpreter import *

class NaviProgram(BoxLayout):
	program = ListProperty([])
	interpreter = Interpreter()

	def add_statement(self, statement):
		self.program.append(statement)
		self.add_widget(Button(text=statement))
		print(self.program)