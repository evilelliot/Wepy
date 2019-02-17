import json
from datetime import datetime

class Format:
	def __init__(self, data):
		self.data   = data
		self.ready  = self.ParseToArray()

	def ParseToArray(self):
		if self.data == "error:404":
			print("Error: config.json not found!")
		else:
			data = json.loads(self.data)
			return data
	
	def GetItem(self, section, wich):	
		return self.ready[section][wich]

	def GetSingle(self, section):	
		return self.ready[section]

	def ConcatItems(self, name, a, b):
		return str(name + ": " + a + ", " + b)

	def unixt(self, unix):
		return datetime.fromtimestamp(int(unix)).strftime('%Y-%m-%d %H:%M:%S')
	