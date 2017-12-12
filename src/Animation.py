class Animation:
	def getName(self):
		raise NotImplementedError

	def getBrightness(self):
		return 100

	def getSetupCommand(self):
		return None

	def getAnimationCommand(self):
		raise NotImplementedError

	def getRepeatCount(self):
		return 1