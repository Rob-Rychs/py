import urllib

text = raw_input("Enter some text: ")
connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" + text)
output = connection.read()
connection.close()

if "true" in output:
    print "ALERT !!! This text contains curse word(s)."
else:
    print "Good! This text is free from curse words."
