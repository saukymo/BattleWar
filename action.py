class Action:

	def __init__(self, total_frame):
		self.total_frame = total_frame

	def play():
		pass

class ActionManager:

	def __init__(self):
		self.frame_clock = 0
		self.action_queue = []

	def play(self):
		self.frame_clock += 1
		if self.action_queue[0].play():
			action_queue.pop()
		if len(self.action_queue):
			return False
		return True

	def add_action(action):
		self.action_queue.append(action)
