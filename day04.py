filename="input/day4input.txt"
file=open(filename,"r")
lines=file.readlines()
lines.sort()
guard = 0
start = 0
end = 0
sleepy_data = {}
for line in lines:
	print line
	stuff=line.split(" ")
	day=stuff[0][1:]
	minute=stuff[1][3:][:-1]
	if stuff[2]=='Guard':
		guard=int(stuff[3][1:])
	if stuff[2]=='falls':
		start=int(minute)
	if stuff[2]=='wakes':
		end=int(minute)
		print str(guard) + " was asleep from minute " + str(start) + " to " + str(end)
		time_asleep=end-start
		for i in range(time_asleep):
			print str(guard) + " was asleep in minute " + str(start+i)
			sleepy_data[(day, guard, start+i)]=1
guard_data={}
minute_data={}
for k,v in sleepy_data.iteritems():
	if k[1] in guard_data:
		guard_data[(k[1])] += 1
	else:
		guard_data[(k[1])] = 1
	if (k[1],k[2]) in minute_data:
		minute_data[(k[1], k[2])] += 1
	else:
		minute_data[(k[1], k[2])] =1

biggest_guard=0
biggest_val=0
for k,v in guard_data.iteritems():
	if v > biggest_val:
		biggest_val=v
		biggest_guard=k

biggest_min=0
biggest_val=0
for k,v in minute_data.iteritems():
        if (k[0] == biggest_guard):
		if v > biggest_val:
                	print "for minute: " + str(k[1]) + ", guard " + str(biggest_guard) + " was asleep for " + str(v) + " minutes."
			biggest_val=v
                	biggest_min=k[1]

biggest_all=0
biggest_val=0
for k,v in minute_data.iteritems():
	if v > biggest_val:
		biggest_val=v
		biggest_all=(k[0],k[1])

print "biggest guard: " + str(biggest_guard)
print "biggest minute: " +str(biggest_min)
print "biggest combo: guard #" + str(biggest_all[0]) +", on minute " + str(biggest_all[1])
