# Import Kivy functionality
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, NumericProperty, StringProperty, ObjectProperty

class ProgramBlock(Button):
	'''
	An entity class that models a single program block that can be drag-and-dropped
	from the NaviBlocks area to the NaviProgram area.
	'''
	selected = BooleanProperty(False)
	originX = NumericProperty(None)
	originY = NumericProperty(None)
	
	def set_origin(self):
		'''
		Sets the origin of the block so that it knows where to return to.
		'''
		self.originX = self.center_x
		self.originY = self.center_y

	def on_touch_down(self, touch):
		'''
		On touching down, the state of the block changes to 'selected' and it's origin is remembered.
		'''
		if self.collide_point(touch.x, touch.y):
			self.set_origin()
			self.selected = True
			#print('selected!')

	def on_touch_move(self, touch):
		'''
		When the touch moves, set the block to follow the touch position.
		'''
		if self.selected:
			self.center_x = touch.x
			self.center_y = touch.y

	def on_touch_up(self, touch):
		'''
		When the touch is up, set 'selected' to False, and return the block to its original position.
		'''
		if self.selected:
			self.selected = False
			#	print('not selected!')
			self.reset_position()

	def reset_position(self):
		'''
		A function that returns the block back to its original position.
		'''
		self.center_x = self.originX
		self.center_y = self.originY