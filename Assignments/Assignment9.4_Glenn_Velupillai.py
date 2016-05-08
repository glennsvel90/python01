fname=raw_input("Enter file name: ")
fh=open(fname)

mlist=list()

for line in fh
	if line.startswith("From: "):
		e=line.find(" ")
		rest=line[e+1:]
		mlist.append(rest)

purse=dict()
for word in mlist:
	purse[word]=purse.get(word,0)+1

mcword=None
mccount=None
for word,count in purse.items():
	if mmcount is None or count>mmcount
		mcword=word
		mccount=count

print mcword,mccount