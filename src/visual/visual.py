import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

class Visual:
	def __init__(self):
		pass
	def Welcome(self):
		print("----------------------------------------------------------------")
		print("----------------------------------------------------------------")
		print("----------------------------------------------------------------")
		cprint(figlet_format("  Wepy  " , font='starwars'), 'yellow', 'on_blue', attrs=['bold'])
		print("----------------------------------------------------------------")
		print("----------------------------------------------------------------")
		print("----------------------------------------------------------------")
	def ShowData(self, data):
		for (slug, title) in sorted(data.items()):
			print("> " + title)
		