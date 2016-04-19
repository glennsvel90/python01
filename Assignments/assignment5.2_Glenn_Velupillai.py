nums=[]
largest=None
smallest=None

def done(largest,smallest):

		print"Highest number is: ", (largest)
		print"Lowest number is: ", (smallest)

while True:
	put =raw_input("Enter a number ")

	if put=="Done":
	
		break

	try:
		integ=float(put)
	except:
		print "Invalid number, please input an integer"
		continue

		nums.append(put)
	for num in nums:
		
		if num>largest:
			largest=num
			
		if num<smallest:
			smallest=num

done(largest,smallest)


