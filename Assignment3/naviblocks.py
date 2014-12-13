from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class NaviBlocks(BoxLayout):
	move_block = ObjectProperty(None)
	turn_block = ObjectProperty(None)
	misc1 = ObjectProperty(None)
	misc2 = ObjectProperty(None)
	misc3 = ObjectProperty(None)