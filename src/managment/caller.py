import json
import urllib.request
import urllib.parse

class Caller:
	def __init__(self):
		self.init = 3009
	def APICall(self, url, city, cc, api):
		completeURL = url + city + "," + cc + "&appid=" + api

		request  = urllib.request.urlopen(str(completeURL))
		response = request.read().decode("utf-8")
		return response
		
