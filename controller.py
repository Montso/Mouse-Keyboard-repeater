'''
Controls mouse and keyboard
'''
from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyboardController
from log_parser import Parse
import pdb, math
from time import sleep


class Mouse:

	def __init__(self):		
		self.mouse = mouseController()


	def pos(self, x, y):
		self.mouse.position = (math.floor(x*0.7), math.floor(y*0.7))
		print(x,y)

	def click(self, button):
		self.mouse.press(button)

	def release(self, button):
		self.mouse.release(button)

	def scroll(self, dy):
		self.mouse.scroll(0,dy)


	def run(self, cmd):
		if cmd["event"] == "click":
			if cmd["button"] == "Button.left":
				button = Button.left
			elif cmd["button"] == "Button.right":
				button = Button.right

			#check command: click or release?	
			if cmd["status"] == "True":
				self.click(button)
			elif cmd["status"] == "False":
				self.release(button)

		elif cmd["event"] == "scroll":
			self.scroll(cmd["dy"])

		elif cmd["event"] == "move":
			self.pos(cmd["x"], cmd["y"])



class Keyboard:

	def __init__(self):
		self.keyboard = keyboardController()

	def press(self, key):
		self.keyboard.press(key)

	def release(self, key):
		self.keyboard.release(key)
	
mouse = Mouse()
controllers = {"mouse": mouse.run}

with open("logs/log.txt", "r") as file:
	logs = file.readlines()
	file.close()

sleep(3)
for log in logs:

	parse = Parse(log)
	command = parse.command
	controllers[command["obj"]](command)

	#break on last command
	if float(parse.deltaTime) == -1.0:
		print('Done')
		break

