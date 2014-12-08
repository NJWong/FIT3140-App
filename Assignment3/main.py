class main:
	def __init__(self, robot, maze):
		self.robot = robot
		self.maze = maze

	def move_robot_forward(self):
		self.robot.move_forward()