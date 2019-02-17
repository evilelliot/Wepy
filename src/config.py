#--- Clase de configuración
import sys
import json
import os.path
from pprint import pprint


class Config:
	Error = ""
	def __init__(self):
		if self.CheckConfiguration():
			with open('config.json') as file:
				data = json.load(file)
				self.config = data
		else: 
			sys.exit("Error: config.json not found!")

	def Data(self, wich):
		return self.config[wich]

	def CheckConfiguration(self):
		if os.path.exists("config.json"):
			return True
		else:
			return False
		
			