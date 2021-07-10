'''
Parses logs into controller
'''
from datetime import datetime
import json
import pdb

class Parse:

	def __init__(self, log):

		self.deltaTime, self.command_str = log.split('|')
		self.command_str = self.command_str.replace("\'", "\"")#preparing string repr for json fconversion - double quotes
		self.command = json.loads(self.command_str) #convert dict string representations to dictionaries
		self.obj = self.command["obj"]

if __name__ == '__main__':
	parse = Parse("-1|{'obj': 'mouse', 'event': 'move', 'x': 1580, 'y': 254}")