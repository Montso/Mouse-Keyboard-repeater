from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyboardController
from log_parser import Parse
import pdb
from time import sleep
# pdb.set_trace()


class Mouse:

	def __init__(self):		
		self.mouse = mouseController()

	def pos(self, x, y):
		pass#self.mouse.position = (10, 20)

	def move(self, x, y):
		self.mouse.move(x, y)

	def click(self, button):
		self.mouse.press(button)

	def release(self, button):
		self.mouse.release(button)

	def scroll(self, dy):
		self.mouse.scroll(0,dy)


	def run(self, cmd):
		if cmd["event"] == "click":
			if cmd["status"] == True:
				self.click(cmd["button"])
			elif cmd["status"] == False:
				self.release(cmd["button"])

		elif cmd["event"] == "scroll":
			self.scroll(cmd["dy"])

		elif cmd["event"] == "move":
			self.move(cmd["x"], cmd["y"])



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


for log in logs:
	
	# pdb.set_trace()
	parse = Parse(log)
	command = parse.command
	controllers[command["obj"]](command)
	sleep(parse.deltaTime)
