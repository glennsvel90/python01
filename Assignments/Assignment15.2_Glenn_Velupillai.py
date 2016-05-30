import urllib
import json

url=raw_input("Enter Url: ")
o=urllib.urlopen(url)
r=o.read()
load=json.loads(str(r))

counts=[]
colls=load["comments"]

for coll in colls:
	counts.append(coll["count"])

print sum(counts)

