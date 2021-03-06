# Import other python classes
from interpreter import *
from programblock import *
from cleartile import *
from walltile import *
from goaltile import *
from navimaze import *
from naviprogram import *
from naviblocks import *
from navicontrols import *

# Import kivy functionality
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock
from functools import partial

class NaviBot(FloatLayout):
	'''
	The main class that controls the flow of the application. Implemented as a Kivy FloatLayout Widget.
	Takes the program defined in NaviProgram and passes it statement by statement to the Interpreter
	for execution. Application state (maze, robot location, etc.) is then modified from here.
	'''
	naviblocks = ObjectProperty(None)
	naviprogram = ObjectProperty(None)
	navicontrols = ObjectProperty(None)
	navimaze = ObjectProperty(None)
	interpreter = Interpreter()
	execution_tree = ListProperty(None)

	def run_program(self, program):
		'''
		Take the program defined in NaviProgram and pass it to the interpreter to run.
		'''
		self.execution_tree = self.interpreter.create_execution_tree(self.naviprogram.program)
		
		# Setting up a clock schedule for each statement so there is a visible delay between statement execution.
		for i in range(len(self.execution_tree)):
			try:
				Clock.schedule_once(partial(self.run, self.execution_tree[i]), i)
			except KeyError:
				print('Unknown statement: skipping execution')

	def run(self, statement, dt):
		'''
		Each statement that the interpreter evaluates returns as a function to modify application state.
		This function is then executed here.
		'''
		exec(statement)

class NaviBotApp(App):
	def build(self):
		navibot = NaviBot()
		navibot.navimaze.initialize()
		return navibot

if __name__ == '__main__':
	NaviBotApp().run()