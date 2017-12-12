from PIL import Image

from led_matrix_client import Command

from Animation import Animation

SNOW_COORDS = [
	(4, 1),
	(59, 2),
	(31, 3),
	(17, 5),
	(52, 5),
	(36, 9),
	(11, 10),
	(49, 13),
	(26, 14),
	(7, 16),
	(34, 19),
	(23, 20),
	(3, 21),
	(44, 24),
	(14, 12),
	(27, 27),
	(59, 28),
	(43, 30),
	(10, 31)
]

ROWS = 32

class HappyHolidaysAnimation(Animation):
	def getName(self):
		return "happy-holidays"

	def getBrightness(self):
		return 80

	def getSetupCommand(self):
		happyHolidays = Image.open("./img/happy-holidays.png")
		return Command.defineImage("happy-holidays", happyHolidays)

	def getAnimationCommand(self):
		commands = []
		for i in range(63, 0, -1):
			commands.append(Command.clear())
			commands.append(Command.image(i, 0, "happy-holidays"))
			commands.append(Command.show())
			commands.append(Command.sleep(25))

		commands.append(Command.sleep(2000))

		for i in range(0, -62, -1):
			commands.append(Command.clear())
			commands.append(Command.image(i, 0, "happy-holidays"))
			commands.append(Command.show())
			commands.append(Command.sleep(25))

		return Command.composite(commands)

	def getRepeatCount(self):
		return 1