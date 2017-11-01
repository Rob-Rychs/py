from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

try:
    word = input("Enter word: ")
    url = "http://www.dictionary.com/browse/" + word
    html = urlopen(url).read()
    data = html.decode('utf-8')

    bs_obj = BeautifulSoup(data, "html.parser")
    defs = bs_obj.findAll("div", {"class" : "def-content"})
    count = 0

    for x in defs:
        count += 1
        st = x.getText()[10:]
        #print (st)
        m = re.search(":   ", st)
        if m == None:
            print (str(count)+ ": " + st)
        else:
            end = m.start()
            new = st[0:end]
            print(str(count) + ": " + new)
        if count > 2:
            break
except:
    print ("Sorry we can't find this word.")
