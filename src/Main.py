from led_matrix_client import NetworkClient, Command
from LetItSnow import LetItSnowAnimation
from HappyHolidays import HappyHolidaysAnimation

ANIMATIONS = [HappyHolidaysAnimation(), LetItSnowAnimation()]


def defineAnimations(client):
	for animation in ANIMATIONS:
		if (animation.getSetupCommand() != None):
			client.sendCommand(animation.getSetupCommand())
		client.sendCommand(Command.defineAnimation(animation.getName(), animation.getAnimationCommand()))


def playAnimations(client):
	while True:
		for animation in ANIMATIONS:
			client.sendCommand(Command.brightness(animation.getBrightness()))
			for count in range(0, animation.getRepeatCount()):
				client.sendCommand(Command.animation(animation.getName()))


client = NetworkClient("localhost", 1236)
defineAnimations(client)
playAnimations(client)

client.close()
