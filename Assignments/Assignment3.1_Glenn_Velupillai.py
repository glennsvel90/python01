hours = raw_input('Enter hours:')
pay = raw_input('Enter pay rate:')

if hours > 40 :
	total=((40*float(pay))+(float(hours) - 40)*1.5*float(pay))
else :
	total=float(hours)*float(pay)

print 'Hey I owe you ', total