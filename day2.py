filename="input/day2input.txt"
file=open(filename,"r")
two_exist = 0
three_exist = 0
for line in file:
	chara = {}
	for c in line:
		if c in chara:
			chara[c] += 1
		else:
			chara[c] = 1
	if 2 in chara.values():
		two_exist += 1
	if 3 in chara.values():
		three_exist += 1

print str(two_exist) + " have two, " + str(three_exist) + " have three."
print "Checksum equals: " + str(two_exist * three_exist)
