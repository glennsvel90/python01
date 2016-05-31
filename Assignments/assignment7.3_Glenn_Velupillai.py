fh=open("mbox-short.txt")
numl=[]

for line in fh:
	line = line.strip()
	if line.startswith("X-DSPAM-Confidence:"):
		decimal=line.find(".")
		number=line[decimal:]
		number=float(number)
		numl.append(number)

<<<<<<< HEAD
	number = float(line[line+1:])
=======
>>>>>>> ee8ef3d17efb8a8bb54fa6829aa4f1dacec6b6ac

count = 0
sumof = 0
for value in numl:
	count =count+1
	sumof= sumof +value
print sumof / count

