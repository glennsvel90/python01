
text = "X-DSPAM-Confidence: 0.8475"
#                 1         2  
#       0123456789012345678901234567890
 
decimal= text.find(".")
number = float(text[decimal:])
type(number)

print number