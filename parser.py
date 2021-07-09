from datetime import datetime
import json

class Parse:

	def __init__(self, log):

		self.deltaTime, self.command_str = log.split('|')
		self.command_str = self.command_str.replace("\'", "\"")#convert to json format
		self.command = json.loads(self.command_str) #convert dict string representations to dictionaries
		self.obj = self.command["obj"]

		print(self.command)
		return self.command
	
	# def mouse_move(self):
	# 	return self.command["x"], self.command["y"]

	# def mouse_scroll(self):
	# 	return self.command["dy"]

	# def mouse_click(self):
	# 	return self.command["button"],

	# def key_event(self):
	# 	return self.command["event"], self.command["key"]

if __name__ == '__main__':
	parse = Parse("-1|{'obj': 'mouse', 'event': 'move', 'x': 1580, 'y': 254}")