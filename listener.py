from pynput import keyboard, mouse
import logging
import log_compiler

logging.basicConfig(filename="temp/log.txt", level=logging.DEBUG, format='%(asctime)s|%(message)s')

class Mouse():


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

	def __init__(self):
		self.obj = "keyboard"

	def on_press(self, key):
		try:
			print("key pressed: {0}".format(key.char))
			event = {
				"obj": self.obj,
				"event": "p",
				"key": key.char
		        }
			logging.debug(event)

		except:
			print("Special key pressed: {0}".format(key))

			event = {
				"obj": self.obj,
				"event": "p",
				"key": str(key)
		        }
			logging.debug(event)

	def on_rel(self, key):
		try:
			print("key released: {0}".format(key))
			event = {
				"obj": self.obj,
				"event": "r",
				"key": key.char
		        }
			logging.debug(event)
		except:
			print("Special key released: {0}".format(key))
			event = {
				"obj": self.obj,
				"event": "r",
				"key": str(key)
				}
			logging.debug(event)

		#exist on ESC
		if key == keyboard.Key.esc:
			return False

def main():
	keyB = Keyboard()
	mous = Mouse()
	with keyboard.Listener(on_press=keyB.on_press, on_release=keyB.on_rel) as listner:
		with mouse.Listener(on_move=mous.on_move, on_scroll=mous.on_scroll) as listner:
			listner.join()

if __name__ == '__main__':
	main()
log_compiler.main()