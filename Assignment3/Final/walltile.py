from kivy.uix.button import Button
from kivy.properties import BooleanProperty

class WallTile(Button):
	collide = BooleanProperty(True)