# Import Kivy functionality
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class NaviBlocks(BoxLayout):
	'''
	The application area that defines the ProgramBlocks available
	to the user. Defines blocks as ObjectProperties.
	'''
	move_block = ObjectProperty(None)
	turn_block = ObjectProperty(None)
	distance_to_wall = ObjectProperty(None)
	
	# Below are dummy ProgramBlocks to show that this class is easy to extend.
	distance_to_goal = ObjectProperty(None)