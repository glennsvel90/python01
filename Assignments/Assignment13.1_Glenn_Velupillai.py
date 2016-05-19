
import re
import urllib
from BeautifulSoup import *

url=raw_input("Enter - ")
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)




numlst=re.findall("^<tr><td><span class=\"comments\">([0-9]+)</span>",html)
n=list()
for i in numlst:
	i=int(i)
	n.append(i)
nn=sum(n)
print nn
