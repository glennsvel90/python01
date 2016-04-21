nums=[]

def done(largest,smallest):
		print"Highest number is: ", (largest)
		print"Lowest number is: ", (smallest)

while True:
	put =raw_input("Enter a number ")
	if put=="Done":
		if nums==[]:
			print "Error, you entered no numbers"
			continue
		else:
			break
	else:
		try:
			integ=float(put)
		except:
			print "Invalid number, please input an integer"
			continue
		nums.append(put)
		largest = max(nums)
		smallest = min(nums)

done(largest,smallest)





