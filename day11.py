grid={}
summedGrid={}
serialNumber=7511

for x in range(1,301):
    if x==1:
        running=0
    else:
        running=summedGrid[(x-1,1)]['value']
    for y in range(1,301):
        rackId = x + 10
        powerLevel = rackId * y
        powerLevel += serialNumber
        powerLevel = powerLevel * rackId
        powerLevel = int(str(powerLevel)[-3])
        powerLevel -= 5
        grid[(x,y)]= {'powerLevel': powerLevel}
        if x==1:
            running += grid[(x,y)]['powerLevel']
        elif y==1:
            running += grid[(x,y)]['powerLevel']
        else:
            running = summedGrid[(x-1,y)]['value'] + summedGrid[(x,y-1)]['value'] - summedGrid[(x-1,y-1)]['value'] + grid[(x,y)]['powerLevel']
        summedGrid[(x,y)]={'value': running}
print "grid generated"

highestTotal=0
for n in range(2,300):
    for x in range(1,301-n):
        for y in range(1,301-n):
            if x==1:
                if y==1:
                    tot=summedGrid[(x+n,y+n)]['value']
                else:
                    tot=summedGrid[(x+n,y+n)]['value']-summedGrid[(x+n,y-1)]['value']
            elif y==1:
                tot=summedGrid[(x+n,y+n)]['value']-summedGrid[(x-1,y+n)]['value']
            else:
                tot=summedGrid[(x+n,y+n)]['value']+summedGrid[(x-1,y-1)]['value']-summedGrid[(x-1,y+n)]['value']-summedGrid[(x+n,y-1)]['value']
            if tot>highestTotal:
                print "("+str(x)+","+str(y)+","+str(n+1)+"): "+str(tot)
                highestTotal=tot