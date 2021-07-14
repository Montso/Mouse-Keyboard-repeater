'''
Controls mouse and keyboard
'''
from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyboardController
from log_parser import Parse
import ctypes
from time import sleep

# Screen resolution awareness
PROCESS_PER_MONITOR_DIP_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DIP_AWARE)

class Mouse:

	def __init__(self):		
		self.mouse = mouseController()
		self.buttons = {"Button.left": Button.left, "Button.right": Button.right}

	def pos(self, x, y):
		self.mouse.position = (x, y)
		print(x,y)

	def click(self, button):
		self.mouse.press(button)

	def release(self, button):
		self.mouse.release(button)

	def scroll(self, dy):
		self.mouse.scroll(0,dy)


	def run(self, cmd):
		if cmd["event"] == "start_position":
			self.pos(cmd["x"], cmd["y"])
				

		if cmd["event"] == "click":
			button_str = cmd["button"]
			button = self.buttons[button_str]

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

		# Special keys objects
		self.special_keys = {'alt': Key.alt, 'alt_gr': Key.alt_gr, 'alt_l': Key.alt_l, 'alt_r': Key.alt_r, 'backspace': Key.backspace,
		 'caps_lock': Key.caps_lock, 'cmd': Key.cmd, 'cmd_r': Key.cmd_r, 'ctrl': Key.ctrl, 'ctrl_l': Key.ctrl_l, 'ctrl_r': Key.ctrl_r,
		  'delete': Key.delete, 'down': Key.down, 'end': Key.end, 'enter': Key.enter, 'esc': Key.esc, 'f1': Key.f1, 'f10': Key.f10,
		   'f11': Key.f11, 'f12': Key.f12, 'f13': Key.f13, 'f14': Key.f14, 'f15': Key.f15, 'f16': Key.f16, 'f17': Key.f17, 'f18': Key.f18,
		    'f19': Key.f19, 'f2': Key.f2, 'f20': Key.f20, 'f21': Key.f21, 'f22': Key.f22, 'f23': Key.f23, 'f24': Key.f24, 'f3': Key.f3,
		     'f4': Key.f4, 'f5': Key.f5, 'f6': Key.f6, 'f7': Key.f7, 'f8': Key.f8, 'f9': Key.f9, 'home': Key.home, 'insert': Key.insert,
		      'left': Key.left, 'media_next': Key.media_next, 'media_play_pause': Key.media_play_pause, 'media_previous': Key.media_previous,
		       'media_volume_down': Key.media_volume_down, 'media_volume_mute': Key.media_volume_mute, 'media_volume_up': Key.media_volume_up,
		        'menu': Key.menu, 'num_lock': Key.num_lock, 'page_down': Key.page_down, 'page_up': Key.page_up, 'pause': Key.pause,
		         'print_screen': Key.print_screen, 'right': Key.right, 'scroll_lock': Key.scroll_lock, 'shift': Key.shift, 'shift_r': Key.shift_r,
		          'space': Key.space, 'tab': Key.tab, 'up': Key.up}

	def press(self, key):
		self.keyboard.press(key)

	def release(self, key):
		self.keyboard.release(key)
	def run(self, cmd):

		if cmd["event"] == "press":
			try:
				self.press(cmd["key"])
			except:
				self.key = cmd["key"].replace("Key.", "")
				self.press(self.special_keys[self.key])

		elif cmd["event"] == "release":
			try:
				self.release(cmd["key"])
			except:
				self.key = cmd["key"].replace("Key.", "")
				self.release(self.special_keys[self.key])
	
mouse = Mouse()
keyboard = Keyboard()

controllers = {"mouse": mouse.run, "keyboard": keyboard.run}

with open("logs/log.txt", "r") as file:
	logs = file.readlines()
	file.close()

sleep(3)
for log in logs:
	
	try:
		parse = Parse(log)
		command = parse.command
		deltaTime = float(parse.deltaTime)
		controllers[command["obj"]](command)

		# break on last command
		if deltaTime == -1.0:
			print('Done')
			break
		sleep(deltaTime)

	except Exception as e:
		raise e
	finally:
		continue