from robot import *

from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty, NumericProperty, BooleanProperty, DictProperty

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
		self.robot.turn(1,1) # change this to accommodate 'n' rotations

	def turn_anticlockwise(self):
		self.robot.turn(0,1) # change this to accommodate 'n' rotations

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

	def distance_to_wall(self):
		"""
		Return the distance from the robot position to the wall which the robot is currently facing
		"""
		distance = -1
		maze = self.maze 
		x=self.robot.posX
		y=self.robot.posY
		while maze[y][x] != 'W':
			if self.robot.direction=='N':
				y -= 1
			elif self.robot.direction=='E':
				x += 1
			elif self.robot.direction=='S':
				y += 1
			elif self.robot.direction=='W':
				x -= 1
			distance += 1
		return distance

	def detect_win(self):
		"""
		Identify the robot is currently standing on the Goal tile or not,
		if yes, return True (probably later, when detect True, it will call sth to end the app); 
		if not, return False
		"""
		return self.maze.maze[self.robot.posX][self.robot.posY] == 'G'

	def set_temp_maze(self):
		"""
		Create a temp maze for function search to use
		in order not to affect the original maze.
		"""
		temp_maze = [[0 for x in range(self.maze.length)] for x in range(self.maze.length)]

		for row in range(self.maze.length):
			for column in range(self.maze.length):
				temp_maze[row][column] = self.maze.maze[row][column]
		return temp_maze

	def search(self,x,y):
		"""
		Called by distance_to_goal().
		"""
		if self.temp_maze[y][x] == 'G':
			return True
		elif self.temp_maze[y][x] == 'W':
			return False
		elif self.temp_maze[y][x] == 'V':	#the tile has been visited
			return False

		self.temp_maze[y][x] = 'V'
		if (x<self.maze.length-1 and self.search(x+1,y)) or (y>0 and self.search(x,y-1)) or (x>0 and self.search(x-1,y))or (y<self.maze.length-1 and self.search(x,y+1)):
			self.dist += 1
			return True

		return False

	def distance_to_goal(self):
		"""
		call function search(x,y) to use recursive way to solve the maze;
		return the distance from robot position to goal.
		Note: the goal self.collide is False, so only when step on it,
		the function can detect the goal,
		thus it is a bit different from function distance_to_wall
		"""
		self.dist = 0
		self.temp_maze = self.set_temp_maze()
		self.search(self.robot.posX, self.robot.posY)
		return self.dist

	def update_maze(self):
		self.clear_widgets() # inefficient... essentially destroying and recreating objects every call
		for row in self.maze:
			for tile in row:
				self.add_widget(Button(text=tile, background_color=self.tile_dict[tile]))