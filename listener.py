'''
listens to keyboard and mouse events
'''
from pynput import keyboard, mouse
import logging
import log_compiler
from time import sleep

logging.basicConfig(filename="temp/log1.txt", level=logging.DEBUG, format='%(asctime)s|%(message)s')

class Mouse():
	#Mouse listener and logger configurations

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
		print(dx, dy)
		event = {
				"obj": self.obj,
				"event": "scroll",
				"dy": dy
		        }
		logging.debug(event)

	def on_click(self, x, y, button, pressed):
		print(button, pressed)
		event = {
				"obj": self.obj,
				"event": "click",
				"button": str(button),
				"status": str(pressed)
		        }
		logging.debug(event)

		# exist mouse listener on right click
		if button == mouse.Button.right and pressed == True:
			return False

class Keyboard():

	def __init__(self):
		self.obj = "keyboard"

	def on_press(self, key):
		try:
			print("key pressed: {0}".format(key.char))
			event = {
				"obj": self.obj,
				"event": "press",
				"key": key.char
		        }
			logging.debug(event)

		except:
			print("Special key pressed: {0}".format(key))

			event = {
				"obj": self.obj,
				"event": "press",
				"key": str(key)
		        }
			logging.debug(event)

	def on_rel(self, key):
		try:
			print("key released: {0}".format(key))
			event = {
				"obj": self.obj,
				"event": "release",
				"key": key.char
		        }
			logging.debug(event)
		except:
			print("Special key released: {0}".format(key))
			event = {
				"obj": self.obj,
				"event": "release",
				"key": str(key)
				}
			logging.debug(event)

		#exist keyboard listener on ESC
		if key == keyboard.Key.esc:
			return False

def main():
	keyB = Keyboard()
	mous = Mouse()
	with keyboard.Listener(on_press=keyB.on_press, on_release=keyB.on_rel) as listner:
		with mouse.Listener(on_move=mous.on_move, on_scroll=mous.on_scroll, on_click=mous.on_click) as listner:
			listner.join()

if __name__ == '__main__':
	sleep(2)
	main()

log_compiler.main() #compile logs for reading 