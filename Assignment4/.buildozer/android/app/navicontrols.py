# Import Kivy functionality
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class NaviControls(BoxLayout):
	'''
	The program area that holds the control buttons for the application.
	Currently defines Run and Stop.
	'''
	run_button = ObjectProperty(None) # Runs the program
	reset_button = ObjectProperty(None) # reset the program execution (NOT IMPLEMENTED YET!)