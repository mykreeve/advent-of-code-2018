grid={}
summedAreaGrid={}
gridSerialNumber=7511

for x in range(300):
    for y in range(300):
        loc=(x,y)
        rackId = x + 10
        powerLevel = rackId * y
        powerLevel += gridSerialNumber
        powerLevel = powerLevel * rackId
        powerLevel = int(str(powerLevel)[-3])
        powerLevel -= 5
        grid[loc]= {'powerLevel': powerLevel}
print "grid generated"
highestTotal=0

def calcRowStart(y):
    running=0
    for ycalc in range(y):
        running += grid[(0,ycalc)]['powerLevel']
    return running

for y in range(300):
    running=calcRowStart(y)
    for x in range(300):
            running += grid[(x,y)]['powerLevel']
            summedAreaGrid[(x,y)]= {'summedPower': running}

for x in range(2):
    for y in range(300):
        print summedAreaGrid[(x,y)]['summedPower'],
    print "\n"
print "---"
for x in range(2):
    for y in range(300):
        print grid[(x,y)]['powerLevel'],
    print "\n"
input ("")

print "summed area grid complete"

for n in range(297):
    realn=n+3
    print "testing grid size", str(realn)
    for x in range(300-realn):
        for y in range(300-realn):
            
            if (x-1)<0:
                if (y-1)<0:
                    fuelScore=summedAreaGrid[(x+realn, y+realn)]['summedPower']
                else:
                    fuelScore=summedAreaGrid[(x+realn, y+realn)]['summedPower']-summedAreaGrid[(x+realn, y-1)]['summedPower']
            elif (y-1)<0:
                fuelScore=summedAreaGrid[(x+realn, y+realn)]['summedPower']-summedAreaGrid[(x-1, y+realn)]['summedPower']
            else:
                fuelScore=summedAreaGrid[(x+realn, y+realn)]['summedPower']+summedAreaGrid[(x-1, y-1)]['summedPower']-summedAreaGrid[(x+realn, y-1)]['summedPower']-summedAreaGrid[(x-1, y+realn)]['summedPower']

            # print x,y,realn, fuelScore

            # for xran in range(realn):
            #     for yran in range(realn):
            #         fuelScore += grid[(x+xran,y+yran)]['powerLevel']
            if fuelScore >= highestTotal:
                highestTotal = fuelScore
                print "highest to date:", str(highestTotal), " based on location: ", str(x), str(y), " and grid size: ", str(realn)
                # for xranval in range(realn):
                #     for yranval in range(realn):
                #         print grid[(x+xranval,y+yranval)]['powerLevel'],
                # print "\n"
