import main

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout

class NaviBot(FloatLayout):
	naviblocks = ObjectProperty(None)
	naviprogram = ObjectProperty(None)
	navicontrols = ObjectProperty(None)
	#navimaze = ObjectProperty(None)

class Interpreter():
	def __init__(self):
		self.running = False

	def run(self, program):
		for statement in program:
			print(statement)

class NaviProgram(BoxLayout):

	program = ListProperty([])
	interpreter = Interpreter()

	def run_program(self):
		#print('NaviProgram: I am running the program!')
		self.interpreter.run(self.program)

	def stop_program(self):
		print('NaviProgram: I am stopping the progam!')

	def add_statement(self, statement):
		self.program.append(statement)
		self.add_widget(Button(text=statement))
		print(self.program)

class ProgramBlock(Button):
	selected = BooleanProperty(False)
	originX = NumericProperty(None)
	originY = NumericProperty(None)

	def set_origin(self):
		self.originX = self.center_x
		self.originY = self.center_y

	def on_touch_down(self, touch):
		if self.collide_point(touch.x, touch.y):
			self.set_origin()
			self.selected = True

	def on_touch_move(self, touch):
		if self.selected:
			self.center_x = touch.x
			self.center_y = touch.y

	def on_touch_up(self, touch):
		if self.selected:
			self.selected = False
			self.reset_position()

	def reset_position(self):
		self.center_x = self.originX
		self.center_y = self.originY

class NaviBlocks(BoxLayout):
	move_block = ObjectProperty(None)
	turn_block = ObjectProperty(None)
	misc1 = ObjectProperty(None)
	misc2 = ObjectProperty(None)
	misc3 = ObjectProperty(None)

class NaviControls(BoxLayout):
	run_button = ObjectProperty(None)
	stop_button = ObjectProperty(None)

class RunButton(Button):
	pass

class StopButton(Button):
	pass

class NaviMaze(GridLayout):
	pass

class NaviBotApp(App):
	def build(self):
		navibot = NaviBot()
		return navibot

if __name__ == '__main__':
	NaviBotApp().run()