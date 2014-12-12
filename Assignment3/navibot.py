import main

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class NaviBot(FloatLayout):
	#naviblocks = ObjectProperty(None)
	#naviprogram = ObjectProperty(None)
	navicontrols = ObjectProperty(None)
	#navimaze = ObjectProperty(None)

class NaviBlocks(BoxLayout):
	pass

class NaviProgram(StackLayout):
	pass

class NaviControls(BoxLayout):

	run_button = ObjectProperty(None)
	stop_button = ObjectProperty(None)


class NaviMaze(GridLayout):
	pass

class NaviBotApp(App):
	def build(self):
		navibot = NaviBot()
		return navibot

if __name__ == '__main__':
	NaviBotApp().run()