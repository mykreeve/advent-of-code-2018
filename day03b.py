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
file2=open(filename,"r")
for line in file2:
        stuff=line.split(" ")
        claimID=int(stuff[0][1:])
        start=stuff[2].split(",")
        startX=int(start[0])
        startY=int(start[1][:-1])
        size=stuff[3].split("x")
        sizeX=int(size[0])
        sizeY=int(size[1])
	check = 0
        for a in range(sizeX):
                for b in range(sizeY):
			if fabric[(startX+a, startY+b)] > 1:
				check = 1
	if check == 0:
		print "+==+"+str(claimID)+"+==+",
