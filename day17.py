filename="input/day17input.txt"
file=open(filename,"r")
file=file.readlines()

# for my dataset - x from 332 to 615, y from 5 to 2064
minX=330
maxX=616
minY=0
maxY=2065

# for example input - x from 494 to 507, y from 0 to 15
# minX=494
# maxX=507
# minY=0
# maxY=14

earth={}
for x in range(minX, maxX):
    for y in range(minY, maxY):
        earth[x,y]='.'


for line in file:
    line=line.replace('..', ' ').replace(', ', ' ').replace('=',' ').split()
    if line[0]=='y':
        y=int(line[1])
        for x in range (int(line[3]), int(line[4]) + 1):
            earth[x,y]='#'
    if line[0]=='x':
        x=int(line[1])
        for y in range (int(line[3]), int(line[4]) + 1):
            earth[x,y]='#'

earth[500,0]='|'
latest_change=(500,0)

def do_print(earth, latest_change):
    for y in range(latest_change[1]-30,latest_change[1]+30):
        for x in range(latest_change[0]-60,latest_change[0]+40):
            if (x,y) in earth:
                print (earth[x,y], end="")
            else:
                print ("=", end="")
        print ("", end="\n")
    # for y in range(170,190):
    #     for x in range(520,550):
    #         if (x,y) in earth:
    #             print (earth[x,y], end="")
    #         else:
    #             print ("=", end="")
    #     print ("", end="\n")

def count_waters(earth):
    got_to=0
    standing=0
    waters=0
    # manually entered value for lowest y in range below
    for y in range(5,maxY):
        for x in range(minX,maxX):
            if (earth[x,y]=='~' or earth[x,y]=='|'):
                if y>got_to:
                    got_to=y
                waters+=1
            if earth[x,y]=='~':
                standing+=1
    return (standing, waters, got_to)

step=0
while True:
    if step%10==0:
        do_print(earth, latest_change)
        k = count_waters(earth)
        print ("--STATUS UPDATE --- " + str(k[0]) + " standing, " + str(k[1]) + " waters - got to " + str(k[2]) + " out of " + str(maxY-1) )

    for y in range(minY, maxY):
        for x in range(minX, maxX):
            if earth[x,y]=='~':
                # filling gaps
                if (x,y+1) in earth:
                    if earth[x,y+1]=='.' or earth[x,y+1]=='|':
                        print ("filling gap " + str(x) + "," + str(y+1))
                        earth[x,y+1]='~'
                        latest_change=(x,y+1)
                if (x+1,y) in earth:
                    if earth[x+1,y]=='.':
                        print ("filling gap " + str(x+1) + "," + str(y))
                        earth[x+1,y]='~'
                if (x-1,y) in earth:
                    if earth[x-1,y]=='.':
                        print ("filling gap " + str(x-1) + "," + str(y))
                        earth[x-1,y]='~'
            if earth[x,y]=='|':
                if (x,y+1) in earth:
                    if earth[x,y+1]=='.':
                        # water continues flowing down
                        # print("water flows down")
                        earth[x,y+1]='|'
                    if earth[x,y+1]=='#':
                        # water hits clay
                        if earth[x-1,y]=='|' and earth[x+1,y]=='|':
                            pass
                        elif earth[x-1,y]=='|' and earth[x+1,y]=='.' and earth[x+1,y+1]=='.':
                            pass
                        elif earth[x+1,y]=='|' and earth[x-1,y]=='.' and earth[x-1,y+1]=='.':
                            pass
                        else:
                            # print("water hits clay")
                            max=x
                            min=x
                            while earth[max,y] != '#':
                                max += 1
                            while earth[min,y] != '#':
                                min -= 1
                            for i in range(min+1,max):
                                earth[i,y]='~'
                            latest_change=(max,y)
                    if earth[x,y+1]=='~':
                        # water hits standing water
                        if earth[x-1,y]=='|' and earth[x+1,y]=='|':
                            pass
                        elif earth[x-1,y]=='|' and ((earth[x+1,y]=='.' and earth[x+1,y+1]=='.') or (earth[x+1,y]=='#' and earth[x+1,y+1]=='#')):
                            pass
                        elif earth[x+1,y]=='|' and ((earth[x-1,y]=='.' and earth[x-1,y+1]=='.') or (earth[x-1,y]=='#' and earth[x-1,y+1]=='#')):
                            pass
                        else:
                            min=x
                            max=x
                            while (earth[max,y+1]=='~' or earth[max,y+1]=='#') and (earth[max,y]=='.' or earth[max,y]=='|'):
                                max += 1
                            while (earth[min,y+1]=='~' or earth[min,y+1]=='#') and (earth[min,y]=='.' or earth[min,y]=='|'):
                                min -= 1
                            # still contained in clay
                            if earth[min,y]=='#' and earth[max,y]=='#':
                                print ("contained in clay " + str(min+1) + "," + str(y) + " - " + str(max) + "," + str(y))
                                for i in range(min+1,max):
                                    earth[i,y]='~'
                                latest_change=(max,y)
                            # contained in clay on left only
                            if earth[min,y]=='#' and earth[max,y]!='#':
                                print ("contained on left only " + str(min+1) + "," + str(y) + " - " + str(max+1) + "," + str(y))
                                for i in range(min+1,max+1):
                                    earth[i,y]='|'
                                latest_change=(max+1,y)
                            # contained in clay on right only
                            if earth[min,y]!='#' and earth[max,y]=='#':
                                print ("contained on right only " + str(min) + "," + str(y) + " - " + str(max) + "," + str(y))
                                for i in range(min,max):
                                    earth[i,y]='|'                        
                                latest_change=(max,y)
                            # unconstrained flow
                            if earth[min,y]!='#' and earth[max,y]!='#':
                                print ("unconstrained " + str(min) + "," + str(y) + " - " + str(max+1) + "," + str(y))
                                for i in range(min,max+1):
                                    earth[i,y]='|'                      
                                latest_change=(max+1,y)
    step+=1