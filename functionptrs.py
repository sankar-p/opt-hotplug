sysmap = open('System.map', 'r')
fnaddr = open('fnaddress.txt', 'r')

fnptr = {}

for line in sysmap:
	words = line.split()
	fnptr[words[0]] = words[2].rstrip()
	#print words[0], words[2].rstrip()

for line in fnaddr:
	words = line.split()
	word = words[0].rstrip()
	#print word
	print word, fnptr[word]	
