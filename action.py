class Action:

	def __init__(self, total_frame):
		self.total_frame = total_frame

	def play(self):
		pass

class ActionManager:

	def __init__(self):
		self.frame_clock = 0
		self.action_queue = []

	def play(self):
		self.frame_clock += 1
		if len(self.action_queue) == 0:
			return True
		if self.action_queue[0].play():
			self.action_queue.pop(0)
		if len(self.action_queue) == 0:
			return True
		return False

	def add_action(self, action):
		self.action_queue.append(action)

class MoveSightAction(Action):

    def __init__(self, map_manager, target_pos):
        Action.__init__(self, 10)
        self.frame = 0
        self.map_manager = map_manager
        self.target_pos = target_pos

    def play(self):
        assert self.frame != self.total_frame, "Action should be done."
        deltax = (self.target_pos.x - self.map_manager.focus.x) / (self.total_frame - self.frame)
        deltay = (self.target_pos.y - self.map_manager.focus.y) / (self.total_frame - self.frame)
        self.map_manager.focus.x += deltax
        self.map_manager.focus.y += deltay
        self.frame += 1
        if self.frame == self.total_frame:
            return True
        return False