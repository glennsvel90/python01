name = raw_input("Enter file:")
if len(name) < 1 : 
	name = "mbox-short.txt"
handle = open(name)
emails = []

#take away all the spaces before and after the email

for line in handle:
	line=line.strip()

	#if the line starts with "From "(with space)
	if line.startswith('From '):
		#splice the email out
		s_email = line.find(" ")
		e_email = line.find(" ", s_email+1)
		emails.append(line[s_email:e_email])
#make a dictionary and add the emails to 
#dictionary if not in dictionary, and count emails
counts=dict()
for email in emails:
	counts[email] = counts.get(email, 0) + 1

#find the email with the most amounts of counts and print it 

