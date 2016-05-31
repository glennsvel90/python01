import urllib
import xml.etree.ElementTree as ElementTree



lsts=list()
E=raw_input("Enter URL: ")
html= urllib.urlopen(E)




tree=ElementTree.parse(html)

comments=tree.findall('comments/comment')

for comment in comments:
	l=comment.find('count').text
	n=int(l)
	lsts.append(n)

print sum(lsts)