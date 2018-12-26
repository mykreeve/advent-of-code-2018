filename="input/day3input.txt"
file=open(filename,"r")
fabric={}
for line in file:
	stuff=line.split(" ")
	claimID=int(stuff[0][1:])
	start=stuff[2].split(",")
	startX=int(start[0])
	startY=int(start[1][:-1])
	size=stuff[3].split("x")
	sizeX=int(size[0])
	sizeY=int(size[1])
	for a in range(sizeX):
		for b in range(sizeY):
			if (startX+a, startY+b) in fabric:
				fabric[(startX+a, startY+b)] += 1
			else:
				fabric[(startX+a, startY+b)] = 1
twos=0
all=0
for square,value in fabric.iteritems():
	all += 1
	if value>1:
		twos += 1
print twos
print all
