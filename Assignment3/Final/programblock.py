from kivy.uix.button import Button
from kivy.properties import BooleanProperty, NumericProperty

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