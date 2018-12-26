filename="input/day2input.txt"
file=open(filename,"r")
for line in file:
	second=open(filename,"r")
	for line2 in second:
		if line != line2:
			same=0
			for a in range(len(line)):
				if line[a]==line2[a]:
					same += 1
			if same==26:
				print line, line2
