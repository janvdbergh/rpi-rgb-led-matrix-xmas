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

class LetItSnowAnimation(Animation):
	def getName(self):
		return "let-it-snow"

	def getBrightness(self):
		return 80

	def getSetupCommand(self):
		treeInSnow = Image.open("./img/tree-in-snow.png")
		return Command.defineImage("let-it-snow", treeInSnow)

	def getAnimationCommand(self):
		commands = [Command.color(255, 255, 255)]
		for row in range(0, ROWS):
			commands.append(Command.clear())
			commands.append(Command.image(0, 0, "let-it-snow"))
			for snowFlake in SNOW_COORDS:
				x = snowFlake[0]
				y = (snowFlake[1] + row) % ROWS
				commands.append(Command.pixel(x, y))

			commands.append(Command.show())
			commands.append(Command.sleep(200 if row != ROWS - 1 else 50))
		return Command.composite(commands)

	def getRepeatCount(self):
		return 10