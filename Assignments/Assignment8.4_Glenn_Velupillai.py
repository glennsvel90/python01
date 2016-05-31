fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
word_lst = list()


for line in fh:
#splits all the words and puts it in the list
	lst=line.split()
	#lowercase the words and if word is not in the VIP "word 
	# list" 
	# then add the word to the VIP word list
	for word in lst:
		word = word.lower()
		if word not in word_lst:
			word_lst.append(word)

print sorted(word_lst)


