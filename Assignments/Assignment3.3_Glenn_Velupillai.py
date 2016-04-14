score=float (raw_input("Enter Score: "))



if score < 0.0: 
	print "Error, since you entered outside of the range. Please enter score between 0 and 1.0"

if score > 1.0:
	print "Error, since you entered outside of the range. Please enter score between 0 and 1.0"

if score < 0.6 and score >=0.0:
	print 'Your Letter Grade is: F'



if score >= 0.6 and score < 0.7:
	print 'Your Letter Grade is: D'

if score >= 0.7 and score < 0.8:
	print 'Your Letter Grade is: C'

if score >= 0.8 and score < 0.9:
	print ' Your Letter Grade is: B'

if score >= 0.9 and score <= 1.0:
	print ' Your Letter Grade is: A'





