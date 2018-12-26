filename="input/day7input.txt"
file=open(filename,"r")
inputs=[]
for line in file:
	spline=line.split(" ")
	inputs.append((spline[1],spline[7]))

steps=[]
for i in inputs:
	if i[0] not in steps:
		steps.append(i[0])
	if i[1] not in steps:
		steps.append(i[1])

deps=[]
for step in steps:
	deps.append({'step':step, 'depends':[]})
	for i in inputs:
		if step==i[1]:
			for k in deps:
				if k['step']==step:
					k['depends'].append(i[0])
print deps
done={}
for step in steps:
	done[step]=False

def not_done():
	for k,v in done.iteritems():
		if v == False:
			return True
	return False

def get_dependencies(step):
	for d in deps:
		if d['step']==step:
			return d['depends']

def is_step_done(step):
	return done[step]

solution=[]
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while not_done():
	round_not_done=True
	for a in alpha:
		if is_step_done(a)==False and round_not_done:
			dep=get_dependencies(a)
			promising=False
			if len(dep)==0:
				promising=True
			else:
				good=len(dep)
				count=0
				for d in dep:
					if is_step_done(d):
						count += 1
				if count==good:
					promising=True
			if promising==True:
				print a
				done[a]=True
				solution.append(a)
				round_not_done=False

print "".join(solution)

