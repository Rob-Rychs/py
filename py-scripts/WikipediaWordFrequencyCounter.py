# Add the URl in line no.50 you want to crawl and this script will look for data in <p> tag 
# If you want to look for any other tag data change line no.16 'p' to your tag
# It will create crawl.txt file in that directory and will display data


import requests
from bs4 import BeautifulSoup
import operator

fw = open('crawler.txt','w')

def start(url):
	word_list = []
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code,"lxml")
	for all_text in soup.findAll('p'):
		content = all_text.string
		if str(content) != 'None':
			words = content.lower().split()
			for each_word in words:
				word_list.append(each_word)
	clean_up_list(word_list)

def clean_up_list(word_list):
	clean_word_list = []
	for word in word_list:
		symbols = "~!@#$%^&*()_+{}|:\"<>?/.,;'[]\=-`'"
		for i in range(0, len(symbols)):
			word = word.replace(symbols[i],'')
		if len(word) > 0 :
			fw.write(word)
			fw.write('  ')
			clean_word_list.append(word) 
	create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
	word_count = {}
	for word in clean_word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

	for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
		fw.write(key)
		fw.write(' ')
		fw.write(str(value))
		fw.write('\n')

start('Your URL here')