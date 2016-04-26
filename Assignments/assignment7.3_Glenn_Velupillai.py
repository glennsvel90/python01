file_name=raw_input("Enter file name: ")
fh=open(file_name)

for line in fh:
	decimal=line.find(.)
	number=float(line[decimal:])

