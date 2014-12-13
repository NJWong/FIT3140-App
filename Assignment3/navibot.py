import main

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, BooleanProperty, DictProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout

class NaviBot(FloatLayout):
	naviblocks = ObjectProperty(None)
	naviprogram = ObjectProperty(None)
	navicontrols = ObjectProperty(None)
	navimaze = ObjectProperty(None)

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

class ClearTile(Button):
	collide = BooleanProperty(False)

class WallTile(Button):
	collide = BooleanProperty(True)

class GoalTile(Button):
	collide = BooleanProperty(False)

class Robot(Button):
	posX = NumericProperty(0) # Hard coded for now
	posY = NumericProperty(0) # Hard coded for now
	direction = StringProperty('E') # Hard coded for now
	direction_list = ListProperty(['N', 'E', 'S', 'W'])

	def move_forward(self):
		if self.direction == 'N':
			self.posY -= 1
		elif self.direction == 'E':
			self.posX += 1
		elif self.direction == 'S':
			self.posY += 1
		elif self.direction == 'W':
			self.posX -= 1
		else:
			print('invalid direction')

	def turn(self, clockwise_flag, n):
		# TODO: could optimise the assignments and checking here
		for i in range(n):
			current_dir = self.direction_list.index(self.direction)
			# if clockwise == 1, turn clockwise
			if clockwise_flag == 1:
				new_dir = (current_dir + 1) % 4
			# if clockwise == 0, turn anticlockwise
			elif clockwise_flag == 0:
				new_dir = (current_dir - 1) % 4
			else:
				print("robot -> turn(): invalid clockwise_flag value")
				new_dir = current_dir

			self.direction = self.direction_list[new_dir]

class NaviMaze(GridLayout):
	maze = ListProperty([
			['C','C','C','W','W'],
			['W','W','C','W','W'],
			['W','W','C','W','W'],
			['W','W','C','G','W'],
			['W','W','W','W','W']])
	maze_length = NumericProperty(4)
	generated = BooleanProperty(False)
	tile_dict = DictProperty({'C':(0,1,0,1), 'W':(1,0,0,1), 'G':(0,0,1,1), 'R':(1,1,1,1)})
	robot = Robot()

	def initialize(self):
		self.generate_maze()
		self.insert_robot()

	def generate_maze(self):
		if not self.generated:
			for row in self.maze:
				for tile in row:
					self.add_widget(Button(text=tile, background_color=self.tile_dict[tile]))
			self.generated = True

	def insert_robot(self):
		if self.generated:
			self.maze[self.robot.posY][self.robot.posX] = 'R'
			self.update_maze()

	def turn_clockwise(self):
		self.robot.turn(1,1)

	def turn_anticlockwise(self):
		self.robot.turn(0,1)

	def move_robot(self):
		if self.robot_can_move():
			self.maze[self.robot.posY][self.robot.posX] = 'C'
			self.robot.move_forward()
			self.maze[self.robot.posY][self.robot.posX] = 'R'
			self.update_maze()

	def robot_can_move(self):
		if self.robot.direction == 'N':
			return self.robot.posY > 0 and self.robot.posY <= self.maze_length and not self.detect_wall()
		elif self.robot.direction == 'E':
			return self.robot.posX >= 0 and self.robot.posX < self.maze_length and not self.detect_wall()
		elif self.robot.direction == 'S':
			return self.robot.posY >= 0 and self.robot.posY < self.maze_length and not self.detect_wall()
		elif self.robot.direction == 'W':
			return self.robot.posX > 0 and self.robot.posX <= self.maze_length and not self.detect_wall()

	def detect_wall(self):
		if self.robot.direction=='N':
			return self.maze[self.robot.posY - 1][self.robot.posX] == 'W'
		elif self.robot.direction =='E':
			return self.maze[self.robot.posY][self.robot.posX + 1] == 'W'
		elif self.robot.direction =='S':
			return self.maze[self.robot.posY + 1][self.robot.posX] == 'W'
		elif self.robot.direction =='W':
			return self.maze[self.robot.posY][self.robot.posX - 1] == 'W'

	def update_maze(self):
		self.clear_widgets() # inefficient... essentially destroying and recreating objects every call
		for row in self.maze:
			for tile in row:
				self.add_widget(Button(text=tile, background_color=self.tile_dict[tile]))

class NaviBotApp(App):
	def build(self):
		navibot = NaviBot()
		navibot.navimaze.initialize()
		return navibot

if __name__ == '__main__':
	NaviBotApp().run()