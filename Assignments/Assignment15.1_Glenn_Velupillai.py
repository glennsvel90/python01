import urllib
import json

loc=raw_input("Enter location: ")

serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"

url= serviceurl+urllib.urlencode({"senor": "false", "address" : loc})
o=urllib.urlopen(url)

data=o.read()

js=json.loads(str(data))

print "place ID: ", js["results"][0]["place_id"]