h = raw_input('Enter hours: ')
r = raw_input('Enter pay rate: ')

 
def compute(h,r):

	try:
		h = float(h)
		r = float(r)
	except: 
		return "Error, this is not a number"
	if h > 40 :
		total=((40*r)+(h - 40)*1.5*r)
	else :
		total=h*r
	return "your paycheck is " + str(total)


print compute(h, r)
