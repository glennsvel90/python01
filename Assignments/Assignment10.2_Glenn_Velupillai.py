fname=raw_input("enter file name: ")
fh=open(fname)
purse=dict()
for line in fh:
	lst=line.split()
	wh=lst[5]
	hrlst=wh.split(:)
	hr=hrlist[0]

	purse(hr)=purse.get(hr,0)+1
t=purse.items()
t.sort()
for k, v in t:
	print k,v
