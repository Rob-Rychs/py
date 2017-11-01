#This program prompts you to take break after some fixed interval of time
# This script opens a web browser with that URL
# specify number of breaks required in wanted_break. And time in seconds in time.sleep

import time
import webbrowser

wanted_breaks = 3
curr_break = 0

print('Program started at '+time.ctime())

while(curr_break < wanted_breaks):
	time.sleep(10)

	#Your URl here
	
	webbrowser.open("http://www.facebook.com")
	curr_break += 1
