

import urllib
from BeautifulSoup import *

url=raw_input("Enter - ")
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

#using beaurful spoup to ofind all tags with span
numlst = soup('span')
nn = []
#get text in span and convert to integers
for i in numlst:
	nn.append(int(i.text))

#summing the number

print sum(nn)

