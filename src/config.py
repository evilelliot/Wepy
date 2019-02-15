#--- Clase de configuración
import json
from pprint import pprint

class Config:
	def __init__(self):
		with open('config.json') as file:
			data = json.load(file)
			self.config = data
	
	def Data(self, wich):
		return self.config[wich]
			