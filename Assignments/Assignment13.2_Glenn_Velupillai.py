import urllib
from BeautifulSoup import *

url=raw_input("Enter - ")
count=raw_input("Enter Count: ")

position=raw_input("Enter position: ")

for i in range(1, int(count)):

	html=urllib.urlopen(url).read()

	soup=BeautifulSoup(html)

#using beaurful spoup to ofind all tags with span
	namlst = soup('a')
	url=namlst[int(position)-1]
	print url

print "done", url



