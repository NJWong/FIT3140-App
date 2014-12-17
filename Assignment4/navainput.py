from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.textinput import TextInput


class NaviInput(GridLayout):
	def __init__(self, **kwargs):
		super(kivyentrywidget, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text='What do you want to print?'))
		self.text_input = TextInput(multiline=False)
		self.add_widget(self.text_input)
		self.printbutton = Button(text='Print')
		self.printbutton.bind(on_press=callback)
		self.add_widget(self.printbutton)

	def callback(self):
		return Label(text=self.text_input.text)

class NaviInputApp(App):
	def build(self):
		return NaviInput()