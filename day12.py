filename="input/day12input.txt"
file=open(filename,"r")
proc=file.readlines()
status = "..........................."+proc[0].strip().split(" ")[2]+"..........................."
rules = {}
for n in range(2, len(proc)):
    rules[proc[n].strip().split(" ")[0]] = proc[n].strip().split(" ")[2]
step = 1
print rules
print len(rules)

trig=0
for n in range(len(status)):
    if status[n]=='#' and trig==0:
        posn_first_pot=n
        trig=1


while step<21:
    print step, 
    if step < 10:
        print "",
    print status
    newStatus = list(status)
    for k,v in rules.iteritems():
        for n in range(len(status)-5):
            testString=status[n:n+5]
            if testString==k:
                newStatus[n+2]=v
    status="".join(newStatus)
    step += 1

sum=0
testStatus=list(status)
for n in range(len(status)):
    if testStatus[n]=="#":
        print (n-posn_first_pot+1),
        sum += (n-posn_first_pot+1)

print ": " + str(sum)
