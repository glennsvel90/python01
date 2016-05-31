file_name=raw_input("Enter file name: ")
fh=open('mbox-short.txt')
numl=[]
count=0
sum=0
for line in fh:

	line= "mbox-short.txt".find(".")
	n=float(line)

	number = float(line[line+1:])

	put=type(number)
	numl.append(put)
print "Before", count, sum
for value in numl:
	count =count+1
	sum= sum+value
	print count, sum, value
print "After", count, sum, sum / count

