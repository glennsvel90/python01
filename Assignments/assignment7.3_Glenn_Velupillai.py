file_name=raw_input("Enter file name: ")
<<<<<<< HEAD
fh=open(file_name)

for line in fh:
	decimal=line.find(.)
	number=float(line[decimal:])
=======
fh=open('mbox-short.txt')
numl=[]
count=0
sum=0
for line in fh:

	line= "mbox-short.txt".find(".")
	n=float(line)

	number = float("mbox-short"[line:])

	put=type(number)
	numl.append(put)
print "Before", count, sum
for value in numl:
	count =count+1
	sum= sum+value
	print count, sum, value
print "After", count, sum, sum / count
>>>>>>> ee305d8dc5e532c6d27f4ce28c75e99c0427abbb

