filename="input/day1input.txt"
total=0
done=False
used_freq={}
while done==False:
	file=open(filename,"r")
	for line in file:
		j=int(line)
		total=total+j
		if total in used_freq:
			print "---"+str(total)
			done=True
			break
		else:
			used_freq[total]=1
print total
