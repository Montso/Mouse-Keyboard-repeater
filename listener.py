#import datetime //to get lag time between activities
#from time import sleep
from pynput import keyboard, mouse
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s, %(message)s')


'''
class mous():
	#Mouse activity listener


	def __init__(self):
		pass
	
	def on_move(self,x, y):
		print("moved to {}".format((x, y)))
		logging.info(str((x,y)))


	def on_scroll(x, y, dy):
		print("Scrolled {0} from {1}\n Vector: {2}".format("Down" if dy < 0 else "Up", (x,y), dy))
		logging.info(str((x,y,dy)))
'''

class keyB():
	'''
	keyboard activity listener
	'''

	def __init__(self):
		pass

	def on_press(self, key):
		try:
			print("key pressed: {0}".format(key.char))
			logging.info(str((key.char, "pressed")))
		except:
			print("Special key pressed: {0}".format(key))
			logging.info(str((key, "pressed")))

	def on_rel(self, key):
		try:
			print("key released: {0}".format(key))
			logging.info(str((key.char, "released")))
		except:
			print("Special key released: {0}".format(key))
			logging.info(str((key, "released")))


		#exist on ESC
		if key == keyboard.Key.esc:
			return False

keyB = keyB()
mou = mous()
with keyboard.Listener(on_press=keyB.on_press, on_release=keyB.on_rel) as listner:
	#with mouse.Listener(on_move=mous.on_move, on_scroll=mous.on_scroll) as listner:
	listner.join()

