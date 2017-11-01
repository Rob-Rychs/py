#!/usr/bin/python
#process an image find the hidden morse code then process actual answer
#need to automate this task
import sys
import Image
from math import *
im = Image.open("PNG.png") 
x,y = im.size # get dimension of image (width * height)
pixels = im.load() # get pixels as 2d matrix in "pixels"
count = 0
morse = {
'.-':'A','-...':'B','-.-.':'C','-..':'D',
'.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J',
'-.-':'K','.-..':'L','--':'M','-.':'N','---':'O',
'.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T',
'..-':'U','..-':'V','.--':'W','-..-':'X','-.--':'Y',
'--..':'Z','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5',
'-....':'6','--...':'7','---..':'8','----.':'9','-----':'0',
}
list =[]
for i in range(y):
	for j in range(x):
		if pixels[j,i] == 1:
			count += 1
			if count == 1:                    # No offset for 1st number 
				list.append(i*100 + j)
				anonymous = i*100 + j
			else:
				list.append(i*100 + j -anonymous)
				anonymous = i*100 + j
print "Hidden Message : ",
string =''
for asci in list:
	if asci == 32:
		sys.stdout.write(morse[string])
		string = '' 
	else:
		string += chr(asci)
print ""		
