from interpreter import *
from programblock import *
from cleartile import *
from walltile import *
from goaltile import *
from navimaze import *
from naviprogram import *
from naviblocks import *
from navicontrols import *

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock
from functools import partial

class NaviBot(FloatLayout):
	naviblocks = ObjectProperty(None)
	naviprogram = ObjectProperty(None)
	navicontrols = ObjectProperty(None)
	navimaze = ObjectProperty(None)
	interpreter = Interpreter()
	execution_tree = ListProperty(None)

	def run(self, statement, dt):
		exec(statement)

	def run_program(self, program):
		#print('AUX: run program')
		self.execution_tree = self.interpreter.create_execution_tree(self.naviprogram.program)
		for i in range(len(self.execution_tree)):
			Clock.schedule_once(partial(self.run, self.execution_tree[i]), i)

class NaviBotApp(App):
	def build(self):
		navibot = NaviBot()
		navibot.navimaze.initialize()
		return navibot

if __name__ == '__main__':
	NaviBotApp().run()