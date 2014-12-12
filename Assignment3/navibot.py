import main

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

class NaviBot(FloatLayout):
	#naviblocks = ObjectProperty(None)
	naviprogram = ObjectProperty(None)
	navicontrols = ObjectProperty(None)
	#navimaze = ObjectProperty(None)

	def run(self):
		print('NaviBot: RUN!')

class NaviBlocks(BoxLayout):
	pass

class NaviProgram(StackLayout):
	def run_program(self):
		print('NaviProgram: I am running the program!')

class NaviControls(BoxLayout):
	run_button = ObjectProperty(None)
	stop_button = ObjectProperty(None)

	def run_button_touched(self):
		print('NaviControls: recieved message from RunButton')

	def stop_button_touched(self):
		print('NaviControls: recieved message from StopButton')

class RunButton(Button):
	def on_press(self):
		print('RunButton: Start the program!')

class StopButton(Button):
	def on_press(self):
		print('StopButton: Halt program!')

class NaviMaze(GridLayout):
	pass

class NaviBotApp(App):
	def build(self):
		navibot = NaviBot()
		return navibot

if __name__ == '__main__':
	NaviBotApp().run()