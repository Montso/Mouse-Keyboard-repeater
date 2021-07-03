#import datetime //to get lag time between activities
#from time import sleep
from pynput import keyboard, mouse
import logging

logging.basicConfig(filename="../temp/log.txt", level=logging.DEBUG, format='%(asctime)s|%(message)s')



class Mouse():
	#Mouse activity listener


	def __init__(self):
		self.obj = "mouse"

	def on_move(self, x, y):
		print("moved to {}".format((x, y)))
		event = {
				"obj": self.obj,
				"event": "move",
				"x": x,
				"y": y
		        }
		logging.debug(event)


	def on_scroll(self, x, y, dx, dy):
		print("Scrolled {0} from {1}\n Vector: {2}".format("Down" if dy < 0 else "Up", (x,y), dy))
		event = {
				"obj": self.obj,
				"event": "scroll",
				"dy": x
		        }
		logging.debug(event)


class Keyboard():
	'''
	keyboard activity listener
	'''

	def __init__(self):
		self.obj = "keyboard"

	def on_press(self, key):
		try:
			print("key pressed: {0}".format(key.char))
			event = {
				"obj": self.obj,
				"event": "keypress",
				"key": key.char,
				"status": "p"
		        }
			logging.debug(event)

		except:
			print("Special key pressed: {0}".format(key))

			event = {
				"obj": self.obj,
				"event": "keypress",
				"key": str(key),
				"status": "p"
		        }
			logging.debug(event)

	def on_rel(self, key):
		try:
			print("key released: {0}".format(key))
			event = {
				"obj": self.obj,
				"event": "release",
				"key": key.char,
				"status": "r"
		        }
			logging.debug(event)
		except:
			print("Special key released: {0}".format(key))
			event = {
				"obj": self.obj,
				"event": "release",
				"key": str(key),
				"status": "r"
		        }
			logging.debug(event)


		#exist on ESC
		if key == keyboard.Key.esc:
			return False

keyB = Keyboard()
mous = Mouse()
with keyboard.Listener(on_press=keyB.on_press, on_release=keyB.on_rel) as listner:
	with mouse.Listener(on_move=mous.on_move, on_scroll=mous.on_scroll) as listner:
		listner.join()

