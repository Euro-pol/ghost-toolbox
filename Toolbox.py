from tkinter import *
from tkinter.filedialog import askopenfilename
from pypresence import Presence
import random
import requests
import json
import os
import sys
import base64
import discum
import time

version = "1.5"

primaryBg = "#36393F"
secondaryBg = "#32353B"
tertiaryBg = "#2c2f36"
btnClickColour = "#3e424a"

primaryText = "white"
secondaryText = "#DCDDDE"

client_id = '899359049253015602' #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

def get_random_user_agent():
    userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
    userAgent = random.choice(userAgents)
    return userAgent

class ContextProperties(object):
	@staticmethod
	def encodeData(data):
		binaryData = json.dumps(data).encode()
		encodedData = base64.b64encode(binaryData).decode("utf-8")
		return encodedData

	@staticmethod
	def get(location, guild_id=None, channel_id=None, channel_type=None):
		loc = location.lower()
		if loc == "friends":
			return "eyJsb2NhdGlvbiI6IkZyaWVuZHMifQ==" # {"location":"Friends"}
		elif loc == "context menu":
			return "eyJsb2NhdGlvbiI6IkNvbnRleHRNZW51In0=" # {"location":"ContextMenu"}
		elif loc == "user profile":
			return "eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9" # {"location":"User Profile"}
		elif loc == "add friend":
			return "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==" # {"location":"Add Friend"}
		elif loc == "guild header":
			return "eyJsb2NhdGlvbiI6Ikd1aWxkIEhlYWRlciJ9" # {"location":"Guild Header"}
		elif loc in ("accept invite page", "join guild"):
			data = {
				"location": "Accept Invite Page",
				"location_guild_id": guild_id,
				"location_channel_id": channel_id,
				"location_channel_type": channel_type,
			}
			if loc == "join guild":
				data["location"] = "Join Guild"
			return ContextProperties.encodeData(data)
		else:
			data = {"location":location}
			return ContextProperties.encodeData(data)

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")

  return os.path.join(base_path, relative_path)

if not os.path.isdir(resource_path(os.getenv('APPDATA') + "\GhostToolbox")):
    os.makedirs(resource_path(os.getenv('APPDATA') + "\GhostToolbox"))

def keep_flat(event):       # on click,
    if isinstance(event.widget, Button): # if the click came from the button
        event.widget.config(relief="flat", fg=secondaryText) # enforce an option

def on_enter(e):
    e.widget['background'] = tertiaryBg

def on_leave(e):
    e.widget['background'] = secondaryBg

def randomUserAgent():
        userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
        userAgent = random.choice(userAgents)
        return userAgent

def center_window(window, width=300, height=200):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

bulkTokenCheckerValid = []
bulkTokenCheckerInvalid = []
bulkTokenCheckerIndex = 0
webhookSpammerIndex = 0
serverJoinerIndex = 0
massPingMembers = []
def Main():
    window = Tk()

    def output(text):
        consoleOutput.config(state="normal")
        consoleOutput.insert("end", f"{text}\n")
        consoleOutput.config(state="disabled")
        consoleOutput.see(END)    

    def userLookup():
        def inputResponse(event):
            try:
                userId = consoleInput.get()
                request = requests.get(f"https://discord-lookup.fun/api/user/{userId}")

                if request.status_code == 200:
                    output("[✔] Success, view box below.")
                    output("")
                    output("-----------------User Lookup-----------------")
                    output(f" Username: {request.json()['username']}#{request.json()['discriminator']}")
                    output(f" ID: {request.json()['id']}")
                    output(f" Bot: {request.json()['bot']}")
                    output(f" Public Flags: {request.json()['public_flags']}")
                    output(f" Created At: {request.json()['created_at_nice']}")
                    output("---------------------------------------------")
                    output("")

                else:
                    output("[❌] Failure, couldnt find that user.")

            except:
                output("[❌] Unexpected error happened.")

            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)        

        output("Enter a Discord user ID")
        consoleInput.bind("<Return>", inputResponse)

    def webhookLookup():
        def inputResponse(event):
            webhookUrl = consoleInput.get()
            try:
                request = requests.get(f"https://discord-lookup.fun/api/webhook/{webhookUrl.split('/')[-2]}/{webhookUrl.split('/')[-1]}")

                if request.status_code == 200:
                    output("[✔] Success, view box below.")
                    output("")            
                    output("---------------Webhook Lookup---------------")
                    output(f" Name: {request.json()['name']}")
                    output(f" ID: {request.json()['id']}")
                    output(f" Channel ID: {request.json()['channel_id']}")
                    output(f" Guild ID: {request.json()['guild_id']}")
                    output(f" Created At: {request.json()['created_at_nice']}")
                    output(f" Token: {request.json()['token']}")
                    output("--------------------------------------------")

                else:
                    output("[❌] Failure, couldnt find that webhook.")

            except:
                output("[❌] Unexpected error happened.")

            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)        

        output("Enter a Discord webhook URL")
        consoleInput.bind("<Return>", inputResponse)

    def webhookSpammerSpamWebhook(webhookUrl,message,amountToSpam):
        global webhookSpammerIndex
        webhookSpammerIndex += 1
        request = requests.post(webhookUrl, headers={"Content-Type": "application/json"}, data=json.dumps({"content": message}))
        if request.status_code == 204:
            output("[✔] Successfully sent a message.")
        else:
            output("[❌] Failure, couldnt send a message.")

        rep = window.after(2, webhookSpammerSpamWebhook, webhookUrl, message, amountToSpam)

        if webhookSpammerIndex > amountToSpam:
            window.after_cancel(rep)
            webhookSpammerIndex = 0
            output("Webhook spamming complete!")
            output("")

    def webhookSpammer():
        def inputResponse(event):
            webhookUrl = consoleInput.get()
            consoleInput.delete(0, END)    

            def inputResponse2(event):
                message = consoleInput.get()
                consoleInput.delete(0, END)

                def inputResponse3(event):
                    amountToSpam = int(consoleInput.get())

                    webhookSpammerSpamWebhook(webhookUrl, message, amountToSpam)

                    consoleInput.unbind("<Return>")
                    consoleInput.delete(0, END)        

                output("Enter an amount of messages to spam")
                consoleInput.bind("<Return>", inputResponse3) 

            output("Enter a message to spam")
            consoleInput.bind("<Return>", inputResponse2)             

        output("Enter a Discord webhook URL")
        consoleInput.bind("<Return>", inputResponse)

    def webhookDeleter():
        def inputResponse(event):
            webhookUrl = consoleInput.get()
            try:
                request = requests.delete(webhookUrl)

                if request.status_code == 204:
                    output("[✔] Success, the webhook is now no more!")

                else:
                    output("[❌] Failure, couldnt delete that webhook.")
                    
            except:
                output("[❌] Unexpected error happened.")

            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)        

        output("Enter a Discord webhook URL")
        consoleInput.bind("<Return>", inputResponse)

    def tokenLookup():
        def inputResponse(event):
            try:
                token = consoleInput.get()
                request = requests.get(f"https://discord.com/api/users/@me", headers={"Authorization": token})

                if request.status_code == 200:
                    otherStuff = requests.get(f"https://discord-lookup.fun/api/user/{request.json()['id']}")

                    output("[✔] Success, view box below.")
                    output("")
                    output("----------------Token Lookup-----------------")
                    output(f" Username: {request.json()['username']}#{request.json()['discriminator']}")
                    output(f" Email: {request.json()['email']}")
                    output(f" Phone: {request.json()['phone']}")
                    output(f" ID: {request.json()['id']}")
                    output(f" Bot: {otherStuff.json()['bot']}")
                    output(f" Public Flags: {request.json()['public_flags']}")
                    output(f" Created At: {otherStuff.json()['created_at_nice']}")
                    output("---------------------------------------------")
                    output("")

                else:
                    output("[❌] Failure, the token is invalid.")

            except:
                output("[❌] Unexpected error happened.")

            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)        

        output("Enter a Discord account token")
        consoleInput.bind("<Return>", inputResponse)

    def tokenChecker():
        def inputResponse(event):
            try:
                token = consoleInput.get()
                request = requests.get(f"https://discord.com/api/users/@me/library", headers={"Authorization": token})

                output(f"Checking {token}")

                if request.status_code == 200:
                    output("[✔] The token is valid.")

                else:
                    output("[❌] The token is invalid")

            except:
                output("[❌] Unexpected error happened.")

            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)        

        output("Enter a Discord account token to check")
        consoleInput.bind("<Return>", inputResponse)

    def tokenBanner():
        def inputResponse(event):
            try:
                token = consoleInput.get()

                request = requests.patch(f"https://discord.com/api/users/@me", headers={"Authorization": token, "Content-Type": "application/json"}, data=json.dumps({"data_of_birth": "2014-2-11"}))      

                if request.status_code == 200:
                    output("[✔] Success, the token was banned!")     

                else:
                    output("[❌] Failure, the token wasnt banned.") 

            except:
                output("[❌] Unexpected error happened.")

            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)        

        output("Enter a Discord account token to ban")
        consoleInput.bind("<Return>", inputResponse)

    def testing():
        def inputResponse(event):
            output("You entered: " + str(consoleInput.get()))
            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)

        output("enter something in the input box below")
        consoleInput.bind("<Return>", inputResponse)

    def clearOutput():
        consoleOutput.config(state="normal")
        consoleOutput.delete(0, END)
        consoleOutput.config(state="disabled")

    def changeLog():
        changelogWindow = Toplevel(window)

        Label(changelogWindow, text=f"v{version} Changelog", bg=primaryBg, fg=secondaryText, font=("Segou UI", "14", "normal")).grid(row=0, column=1, sticky="W", pady=(5, 0), padx=(6, 0))
        Label(changelogWindow, text=f"+ Bulk token checker", bg=primaryBg, fg=secondaryText, font=("Segou UI", "8", "normal")).grid(row=3, column=1, sticky="W", pady=(0, 0), padx=(6, 0))
        Label(changelogWindow, text=f"+ Server joiner", bg=primaryBg, fg=secondaryText, font=("Segou UI", "8", "normal")).grid(row=4, column=1, sticky="W", pady=(0, 0), padx=(6, 0))
        Label(changelogWindow, text=f"+ Server leaver", bg=primaryBg, fg=secondaryText, font=("Segou UI", "8", "normal")).grid(row=5, column=1, sticky="W", pady=(0, 0), padx=(6, 0))
        Label(changelogWindow, text=f"+ Channel spammer", bg=primaryBg, fg=secondaryText, font=("Segou UI", "8", "normal")).grid(row=6, column=1, sticky="W", pady=(0, 0), padx=(6, 0))

        changelogWindow.title(f'Ghost Discord Toolbox')
        changelogWindow.configure(bg=primaryBg)
        center_window(changelogWindow, 310, 150)
        changelogWindow.resizable(False, False)
        changelogWindow.iconbitmap(resource_path('icon.ico'))
        changelogWindow.bind('<Button-1>', keep_flat)
        changelogWindow.mainloop()

    def removeOldVersion():
        if os.path.isfile("Ghost Toolbox OLD.exe"):
            os.remove("Ghost Toolbox OLD.exe")   

    def openWindow(title, content, width=500, height=600):
        newWindow = Toplevel(window)

        contentBox = Text(newWindow, width=width, height=height, bg=secondaryBg, fg=secondaryText, relief='flat')
        contentBox.insert(END, content)
        contentBox.pack()

        newWindow.title(f'{title}')
        newWindow.configure(bg=primaryBg)
        center_window(newWindow, width=width, height=height)
        newWindow.resizable(False, False)
        newWindow.iconbitmap(resource_path('icon.ico'))
        newWindow.bind('<Button-1>', keep_flat)
        newWindow.mainloop()        

    def bulkTokenCheckerCheckTokens(tokens):
        global bulkTokenCheckerIndex, bulkTokenCheckerValid, bulkTokenCheckerInvalid
        token = tokens[bulkTokenCheckerIndex]
        bulkTokenCheckerIndex += 1
        request = requests.get("https://discord.com/api/users/@me/library", headers={"Authorization": token})
        if request.status_code == 200:
            output("[✔] Token is valid.")
            bulkTokenCheckerValid.append(token)
        else:
            output("[❌] Token is invalid.")
            bulkTokenCheckerInvalid.append(token)

        rep = window.after(8, bulkTokenCheckerCheckTokens, tokens)

        if bulkTokenCheckerIndex >= len(tokens):
            window.after_cancel(rep)
            bulkTokenCheckerIndex = 0
            output("Bulk token check complete. Opened a list of valid and invalid tokens from the check.")
            output("")
            window.after(50, openWindow, "Invalid Tokens", '\n'.join(bulkTokenCheckerInvalid))
            window.after(50, openWindow, "Valid Tokens", '\n'.join(bulkTokenCheckerValid))
            bulkTokenCheckerValid = []
            bulkTokenCheckerInvalid = []

    def bulkTokenChecker():
        output("Please choose were your tokens file is located.")
        filename = askopenfilename()
        tokens = open(filename).read().splitlines()
        output("Starting check...")
        bulkTokenCheckerCheckTokens(tokens)

    def serverJoinerJoinTokens(tokens, invite):
        
        def joinServer(token, invite):
            invData = requests.get(f"https://discord.com/api/v9/invites/{invite}", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
            guild_id = invData.json()["guild"]["id"]
            channel_id = invData.json()["channel"]["id"]
            channel_type = invData.json()["channel"]["type"]
            headers = {
                "Authorization": token,
                "User-Agent": get_random_user_agent(),
                "X-Context-Properties": ContextProperties.get("join guild", guild_id=guild_id, channel_id=channel_id, channel_type=channel_type)
            }        
            request = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, timeout=0.5)
            return request

        global serverJoinerIndex
        token = tokens[serverJoinerIndex]
        serverJoinerIndex += 1
        try:
            request = joinServer(token, invite)
            if request.status_code == 200:
                output("[✔] Success, joined server.")
            else:
                output("[❌] Failure, failed to join server")
        except:
            output("[❌] Unexpected error happened.")

        rep = window.after(18, serverJoinerJoinTokens, tokens, invite)

        if serverJoinerIndex >= len(tokens):
            window.after_cancel(rep)
            serverJoinerIndex = 0
            output("Server joiner complete!")
            output("")

    def serverJoiner():
        output("Please choose were your tokens file is located.")
        filename = askopenfilename()
        tokens = open(filename).read().splitlines()

        def inputResponse(event):
            invite = consoleInput.get()
            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)            
            output("Starting server joiner...")
            
            serverJoinerJoinTokens(tokens, invite)

        output("Enter a server invite to join")
        consoleInput.bind("<Return>", inputResponse)

    def serverLeaverLeaveTokens(tokens, guildid):
        
        def leaveServer(token, guildid):
            headers = {
                "Authorization": token,
                "User-Agent": get_random_user_agent()
            }        
            request = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guildid}", headers=headers, timeout=0.5)
            return request

        global serverJoinerIndex
        token = tokens[serverJoinerIndex]
        serverJoinerIndex += 1
        try:
            request = leaveServer(token, guildid)
            if request.status_code == 204:
                output("[✔] Success, left server.")
            else:
                output("[❌] Failure, failed to leave server")
        except:
            output("[❌] Unexpected error happened.")

        rep = window.after(50, serverLeaverLeaveTokens, tokens, guildid)

        if serverJoinerIndex >= len(tokens):
            window.after_cancel(rep)
            serverJoinerIndex = 0
            output("Server leaver complete!")
            output("")

    def serverLeaver():
        output("Please choose were your tokens file is located.")
        filename = askopenfilename()
        tokens = open(filename).read().splitlines()

        def inputResponse(event):
            guildId = consoleInput.get()
            consoleInput.unbind("<Return>")
            consoleInput.delete(0, END)            
            output("Starting server leaver...")
            
            serverLeaverLeaveTokens(tokens, guildId)

        output("Enter a server id to leave")
        consoleInput.bind("<Return>", inputResponse)

    def channelSpammerTokenSendMessage(tokens, channelid, content, amount):
        
        def sendMessage(token, channelid, content, amount):
            headers = {
                "Authorization": token,
                "User-Agent": get_random_user_agent(),
                "Content-Type": "application/json"
            }        
            request = requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers, timeout=0.5, data=json.dumps({"content": content}))
            return request

        global serverJoinerIndex
        serverJoinerIndex += 1
        try:
            request = sendMessage(random.choice(tokens), channelid, str(content) + f" [{random.randint(1000, 9999)}]", amount)
            if request.status_code == 200:
                output("[✔] Success, sent message.")
            else:
                output("[❌] Failure, failed to send message.")
        except:
            output("[❌] Unexpected error happened.")

        rep = window.after(2, channelSpammerTokenSendMessage, tokens, channelid, content, amount)

        if serverJoinerIndex >= int(amount):
            window.after_cancel(rep)
            serverJoinerIndex = 0
            output("Channel spammer complete!")
            output("")

    def channelSpammer():
        output("Please choose were your tokens file is located.")
        filename = askopenfilename()
        tokens = open(filename).read().splitlines()

        def inputResponse2(event):
            channelId = consoleInput.get()
            consoleInput.delete(0, END)            
            
            def inputResponse3(event):
                content = consoleInput.get()
                consoleInput.delete(0, END)            
                
                def inputResponse4(event):
                    amount = consoleInput.get()
                    consoleInput.unbind("<Return>")
                    consoleInput.delete(0, END)            
                    
                    channelSpammerTokenSendMessage(tokens, channelId, content, amount)

                output("Enter an amount of messages to send")
                consoleInput.bind("<Return>", inputResponse4)

            output("Enter a message to send")
            consoleInput.bind("<Return>", inputResponse3)

        output("Enter a channel id")
        consoleInput.bind("<Return>", inputResponse2)

    def multiTokenMassPingSendMessages(message, tokens, channelid, amount):
        def sendMessage(token, channelid, content):
            headers = {
                "Authorization": token,
                "User-Agent": get_random_user_agent(),
                "Content-Type": "application/json"
            }        
            request = requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers, timeout=0.5, data=json.dumps({"content": content}))
            return request

        global serverJoinerIndex
        serverJoinerIndex += 1
        request = sendMessage(random.choice(tokens), channelid, message)
        if request.status_code == 200:
            output("[✔] Success, sent message with pings.")
        else:
            output("[❌] Failure, failed to send message with pings.")

        rep = window.after(6, multiTokenMassPingSendMessages, message, tokens, channelid, amount)

        if serverJoinerIndex >= int(amount):
            window.after_cancel(rep)
            serverJoinerIndex = 0
            output("Finished multi token mass ping")
            output("")        

    def multiTokenMassPingFetchMembers(tokens, guildid, channelid, amount):
        headers = {"Content-Type": "application/json"}
        bot = discum.Client(token=tokens[0], user_agent=get_random_user_agent(), log=False)

        def close_after_fetching(resp, guild_id):
            if bot.gateway.finishedMemberFetching(guild_id):
                lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.close()

        def get_members(guild_id, channel_id):
            bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
            bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guild_id).members

        members = get_members(guildid, channelid)
        output(f"Fetched total of {len(members)} members.")
        message = ""
        messages = []
        for memberId in members:
            message += f"<@{memberId}>"
            if len(message) > 1950:
                messages.append(message)
        messages.append(message)
        multiTokenMassPingSendMessages(messages[0], tokens, channelid, amount)        

    def multiTokenMassPing():
        output("Please choose were your tokens file is located.")
        filename = askopenfilename()
        tokens = open(filename).read().splitlines()

        def inputResponse2(event):
            guildId = consoleInput.get()
            consoleInput.delete(0, END)            
            
            def inputResponse3(event):
                channelId = consoleInput.get()
                consoleInput.delete(0, END)          
                
                def inputResponse3(event):
                    amount = consoleInput.get()
                    consoleInput.unbind("<Return>")
                    consoleInput.delete(0, END)          
                    
                    output("Fetching members...")
                    multiTokenMassPingFetchMembers(tokens, guildId, channelId, amount)

                output("Enter of times to send")
                consoleInput.bind("<Return>", inputResponse3)

            output("Enter a channel id to fetch members from")
            consoleInput.bind("<Return>", inputResponse3)

        output("Enter a guild id to fetch members from")
        consoleInput.bind("<Return>", inputResponse2)        

    licenseKey = open(resource_path(os.getenv("APPDATA")+"\GhostToolbox\license.txt")).read()
    titleLabel = Label(window, text="Ghost Toolbox", font=("Segoe UI", "18", "bold"), bg=primaryBg, fg=primaryText).grid(column=1, columnspan=3, pady=24)
    creditsLabel = Label(window, text="Developed by Benny#1430", font=("Segoe UI", "8", "normal"), bg=primaryBg, fg=primaryText).grid(row=999, column=1, columnspan=3)
    Label(window, text="", bg=primaryBg, fg=primaryText).grid(row=1000, column=2)

    consoleOutput = Text(window, height=12, width=40, bg=secondaryBg, fg=secondaryText, relief='flat')
    consoleOutput.grid(row=100, column=1, sticky="EW", columnspan=3, padx=15, pady=(15,0))
    consoleOutput.config(state="disabled")

    consoleInput = Entry(window, bg=secondaryBg, fg=secondaryText, relief='flat')
    consoleInput.grid(row=101, column=1, sticky="EW", columnspan=3, padx=15, pady=(10,15))
    consoleInput.insert(END, "Enter text here.")

    # ------- BUTTONS --------

    webhookLookupBtn = Button(window, text="Webhook Lookup", width=15, command=webhookLookup, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    webhookLookupBtn.grid(row=4, column=1, padx=(15, 2), pady=2, ipadx=5, ipady=8)
    webhookLookupBtn.bind("<Enter>", on_enter)
    webhookLookupBtn.bind("<Leave>", on_leave)

    webhookSpammerBtn = Button(window, text="Webhook Spammer", width=15, command=webhookSpammer, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    webhookSpammerBtn.grid(row=4, column=2, padx=2, pady=2, ipadx=5, ipady=8)
    webhookSpammerBtn.bind("<Enter>", on_enter)
    webhookSpammerBtn.bind("<Leave>", on_leave)

    webhookDeleterBtn = Button(window, text="Webhook Deleter", width=15, command=webhookDeleter, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    webhookDeleterBtn.grid(row=4, column=3, padx=(2, 15), pady=2, ipadx=5, ipady=8)
    webhookDeleterBtn.bind("<Enter>", on_enter)
    webhookDeleterBtn.bind("<Leave>", on_leave)

    tokenLookupBtn = Button(window, text="Token Lookup", width=15, command=tokenLookup, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    tokenLookupBtn.grid(row=5, column=1, padx=(15, 2), pady=2, ipadx=5, ipady=8)
    tokenLookupBtn.bind("<Enter>", on_enter)
    tokenLookupBtn.bind("<Leave>", on_leave)

    tokenCheckerBtn = Button(window, text="Token Checker", width=15, command=tokenChecker, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    tokenCheckerBtn.grid(row=5, column=2, padx=2, pady=2, ipadx=5, ipady=8)
    tokenCheckerBtn.bind("<Enter>", on_enter)
    tokenCheckerBtn.bind("<Leave>", on_leave)

    bulkTokenCheckerBtn = Button(window, text="Bulk Token Checker", width=15, command=bulkTokenChecker, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    bulkTokenCheckerBtn.grid(row=5, column=3, padx=(2, 15), pady=2, ipadx=5, ipady=8)
    bulkTokenCheckerBtn.bind("<Enter>", on_enter)
    bulkTokenCheckerBtn.bind("<Leave>", on_leave)

    tokenBannerBtn = Button(window, text="Token Banner", width=15, command=tokenBanner, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    tokenBannerBtn.grid(row=6, column=1, padx=(15, 2), pady=2, ipadx=5, ipady=8)
    tokenBannerBtn.bind("<Enter>", on_enter)
    tokenBannerBtn.bind("<Leave>", on_leave)

    userLookupBtn = Button(window, text="User Lookup", width=15, command=userLookup, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    userLookupBtn.grid(row=6, column=2, padx=2, pady=2, ipadx=5, ipady=8)
    userLookupBtn.bind("<Enter>", on_enter)
    userLookupBtn.bind("<Leave>", on_leave)

    serverJoinerBtn = Button(window, text="Server Joiner", width=15, command=serverJoiner, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    serverJoinerBtn.grid(row=6, column=3, padx=(2, 15), pady=2, ipadx=5, ipady=8)
    serverJoinerBtn.bind("<Enter>", on_enter)
    serverJoinerBtn.bind("<Leave>", on_leave)

    serverLeaverBtn = Button(window, text="Server Leaver", width=15, command=serverLeaver, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    serverLeaverBtn.grid(row=7, column=1, padx=(15, 2), pady=2, ipadx=5, ipady=8)
    serverLeaverBtn.bind("<Enter>", on_enter)
    serverLeaverBtn.bind("<Leave>", on_leave)

    channelSpammerBtn = Button(window, text="Channel Spammer", width=15, command=channelSpammer, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    channelSpammerBtn.grid(row=7, column=2, padx=2, pady=2, ipadx=5, ipady=8)
    channelSpammerBtn.bind("<Enter>", on_enter)
    channelSpammerBtn.bind("<Leave>", on_leave)

    multiTokenMassPingBtn = Button(window, text="Multi Token Mass Ping", width=15, command=multiTokenMassPing, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat')
    multiTokenMassPingBtn.grid(row=7, column=3, padx=(2, 15), pady=2, ipadx=5, ipady=8)
    multiTokenMassPingBtn.bind("<Enter>", on_enter)
    multiTokenMassPingBtn.bind("<Leave>", on_leave)    

    # Button(window, text="Testing", width=15, command=testing, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat').grid(row=6, column=2, padx=2, pady=2, ipadx=2, ipady=2)
    # Button(window, text="Clear Output", width=15, command=clearOutput, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat').grid(row=6, column=2, padx=2, pady=2, ipadx=2, ipady=2)

    # ------- BUTTONS --------

    RPC.update(details=f"Main menu", state=f"Version {version}", large_image="icon", large_text="Ghost Toolbox")

    window.title(f'Ghost Toolbox [v{version}]')
    window.configure(bg=primaryBg)
    center_window(window, 413, 565)
    window.resizable(False, False)
    window.bind('<Button-1>', keep_flat)
    window.iconbitmap(resource_path('icon.ico'))
    window.after(50, changeLog)
    window.after(1000, removeOldVersion)
    window.mainloop()

def Auth():

    authWindow = Tk()

    def removeOldVersion():
        if os.path.isfile("Ghost Toolbox OLD.exe"):
            os.remove("Ghost Toolbox OLD.exe")

    def login():
        if os.path.isfile(resource_path(os.getenv('APPDATA')+"\GhostToolbox\license.txt")):
            licenseKey = open(resource_path(os.getenv("APPDATA")+"\GhostToolbox\license.txt")).read()
        else:
            licenseKey = keyEntry.get()
        request = requests.get("https://ghost.cool/api/toolbox/get/licenses", headers={"api-key": "1a4ec465-8e5d-4537-8435-95b4e9562698"})
        if licenseKey in request.text:
            RPC.update(details="Auth success.", state=f"Version {version}", large_image="icon", large_text="Ghost Toolbox")
            if not os.path.isfile(resource_path(os.getenv('APPDATA')+"\GhostToolbox\license.txt")):
                licenseFile = open(resource_path(os.getenv("APPDATA")+"\GhostToolbox\license.txt"), "w")
                licenseFile.write(licenseKey)
                licenseFile.close()            
            authWindow.destroy()    
            Main()
        else:
            authWindow.destroy()

    keyLabel = Label(authWindow, text="Enter your license key", bg=primaryBg, fg=secondaryText, font=("Segou UI", "14", "normal"))
    keyLabel.grid(row=0, column=1, sticky="W", pady=(5, 0), padx=(6, 0))
    keyEntry = Entry(authWindow, bg=secondaryBg, fg=secondaryText, relief=FLAT, font=("Segou UI", "14", "normal"))
    keyEntry.grid(row=1, column=1, pady=(5, 4), padx=(6, 0), ipady=6)  

    loginBtn = Button(authWindow, text="Login", command=login, bg=secondaryBg, activebackground=btnClickColour, fg=secondaryText, activeforeground=secondaryText, relief='flat', font=("Segou UI", "14", "normal"))
    loginBtn.grid(row=1, column=3, pady=5, padx=(10, 5))
    loginBtn.bind("<Enter>", on_enter)
    loginBtn.bind("<Leave>", on_leave)

    RPC.update(details="Authentication.", state=f"Version {version}", large_image="icon", large_text="Ghost Toolbox")

    authWindow.title(f'Ghost Discord Toolbox')
    authWindow.configure(bg=primaryBg)
    center_window(authWindow, 310, 85)
    authWindow.resizable(False, False)
    authWindow.iconbitmap(resource_path('icon.ico'))
    authWindow.bind('<Button-1>', keep_flat)
    authWindow.after(1000, removeOldVersion)
    authWindow.mainloop()

def NewVersion(version):
    downloadWindow = Tk()

    def downloadNewVersion():
        os.rename("Ghost Toolbox.exe", "Ghost Toolbox OLD.exe")
        r = requests.get("https://ghost.cool/toolbox/Ghost Toolbox.exe", allow_redirects=True)
        open('Ghost Toolbox.exe', 'wb').write(r.content)
        os.startfile("Ghost Toolbox.exe")
        sys.exit() 

    Label(downloadWindow, text="New version detected", bg=primaryBg, fg=secondaryText, font=("Segou UI", "14", "normal")).grid(row=0, column=1, sticky="W", pady=(5, 0), padx=(6, 0))
    Label(downloadWindow, text=f"This window will close when download is complete.", bg=primaryBg, fg=secondaryText, font=("Segou UI", "8", "normal")).grid(row=1, column=1, sticky="W", pady=(5, 0), padx=(6, 0))
    # Label(downloadWindow, text=f"window will close when download is complete.", bg=primaryBg, fg=secondaryText, font=("Segou UI", "8", "normal")).grid(row=2, column=1, sticky="W", pady=(0, 5), padx=(6, 0))

    downloadWindow.title(f'Ghost Discord Toolbox')
    downloadWindow.configure(bg=primaryBg)
    center_window(downloadWindow, 310, 85)
    downloadWindow.resizable(False, False)
    downloadWindow.iconbitmap(resource_path('icon.ico'))
    downloadWindow.bind('<Button-1>', keep_flat)
    downloadWindow.after(10, downloadNewVersion)
    downloadWindow.mainloop()

Main()