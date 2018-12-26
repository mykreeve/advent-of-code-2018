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
                loc={}
                for item,point in enumerate(points):
                        loc[item]= abs(x-point[0])+abs(y-point[1])
                lowest_item=0
                smallest_value=10000
                for key,value in loc.iteritems():
                        if value==smallest_value:
				lowest_item="n"
			if value<smallest_value:
                                lowest_item=key
                                smallest_value=value
                print str(x) +"," + str(y) + " is closest to point " + str(lowest_item)
		world[(x,y)] = lowest_item

on_the_edge=[]
for x in range(maxX+1):
	if world[(x,0)] not in on_the_edge:
		on_the_edge.append(world[(x,0)])
	if world[(x,maxY)] not in on_the_edge:	
		on_the_edge.append(world[(x,maxY)])
for y in range(maxY+1):
	if world[(0,y)] not in on_the_edge:
		on_the_edge.append(world[(0,y)])
	if world[(maxX,y)] not in on_the_edge:
		on_the_edge.append(world[(maxX,y)])
print on_the_edge

count_item={}
for k,v in world.iteritems():
	if v in count_item:
		count_item[v] += 1
	else:
		count_item[v] = 1

for k,v in count_item.iteritems():
	print str(k) + " is the closest item to " + str(v) + " points",
	if k in on_the_edge:
		print "but we must discount this one"
	print "\n"


