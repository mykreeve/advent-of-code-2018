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

done={}
for step in steps:
	done[step]="n"

def not_done():
	for k,v in done.iteritems():
		if v == "n" or v == "u":
			return True
	return False

def get_dependencies(step):
	for d in deps:
		if d['step']==step:
			return d['depends']

def is_step_done(step):
	return done[step]

def get_next_todo():
	alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for a in alpha:
		if is_step_done(a)=="n":
			dep=get_dependencies(a)
			promising=False
			if len(dep)==0:
				promising=True
			else:
				good=len(dep)
				count=0
				for d in dep:
					if is_step_done(d) == "y":
						count += 1
				if count==good:
					promising=True
			if promising==True:
				return a
	return 'unavailable'

alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha=list(alpha)
print alpha
workers=[]
seconds=0
for w in range(5):
	workers.append({'worker':w, 'doing':'.', 'will_finish':0})
solution=[]

while not_done():
	for w in range(5):
		for k in workers:
			if k['worker']==w:
                                if k['will_finish']==seconds:
                                        done[k['doing']]='y'
					solution.append(k['doing'])
					k['doing']='.'
				if k['doing']=='.':
					next=get_next_todo()
					if next=='unavailable':
						pass
					else:
						k['doing']=next
						done[next]='u'
						for a1,a2 in enumerate(alpha):
							if a2==next:
								k['will_finish']=seconds+60+a1+1
	print seconds,
	for w in range(5):
		for k in workers:
			if k['worker']==w:
				print k['doing'],
	print ""
	seconds += 1


