# Matching two file content...
# A typical Bruteforce script
from itertools import permutations
file1 = open("test1.txt") #file containing jumbled words
file2 = open("wordlist.txt") #file containing real words 
out = open('out.txt','wb')
jwords = [''.join(line.rstrip('\n')) for line in file1]
rwords = [''.join(lines.rstrip('\r\n')) for lines in file2]
print "Writing to file"
for pat in jwords:
	list = [''.join(p) for p in permutations(pat)] 
	list =set(list)
	for words in list:
		for words2 in rwords:
			if words == words2:
				out.write(words +",")
out.close()
file1.close()
file2.close()					
	
