import urllib
from BeautifulSoup import *

url = raw_input("Enter - ")
count = raw_input("count: ")
position = raw_input("Position: ")

count = int(count)
position = int(position)


while count > 0:
  
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    
    url = anchors[position-1]['href']
    count =count- 1

print url


