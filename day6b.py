filename="input/day6input.txt"
file=open(filename,"r")
points=[]
for line in file:
        point=line.rstrip().split(", ")
        points.append((int(point[0]),int(point[1])))

maxX=0
maxY=0
for point in points:
        if point[0] > maxX:
                maxX = point[0]
        if point[1] > maxY:
                maxY = point[1]

print maxX, maxY

world={}
for x in range(maxX+1):
        for y in range(maxY+1):
                distance_to_all=0
                loc={}
                for item,point in enumerate(points):
                        loc[item]= abs(x-point[0])+abs(y-point[1])
                        distance_to_all=distance_to_all + loc[item]
                world[(x,y)]=distance_to_all

in_the_zone=0
for k,v in world.iteritems():
	print str(k) + " - distance: " + str(v)
	if v<10000:
		in_the_zone += 1

print in_the_zone
