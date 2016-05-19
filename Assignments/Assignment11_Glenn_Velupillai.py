import re
fname=raw_input("Enter text file: ")
fh=open(fname)
string=fh.read()
numlst=re.findall("[0-9]+",string)
n=list()
for i in numlst:
	i=int(i)
	n.append(i)

nn=sum(n)

print nn