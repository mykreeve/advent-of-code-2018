import heapq

cave={}
summedCave={}
depth=5616
targetX=10
targetY=785


for x in range(100):
    if x==0:
        running=0
    else:
        running=summedCave[(x-1,0)]['value']
    for y in range(1000):
        if x==0 and y==0:
                geologicalIndex=0
        elif x==targetX and y==targetY:
                geologicalIndex=0
        elif y==0:
                geologicalIndex=x*16807
        elif x==0:
                geologicalIndex=y*48271
        else:
                geologicalIndex=cave[(x-1,y)]['erosionLevel'] * cave[(x,y-1)]['erosionLevel']
        erosionLevel = (geologicalIndex + depth)%20183
        regionType = erosionLevel%3
        cave[(x,y)]= {'geologicalIndex': geologicalIndex, 'erosionLevel': erosionLevel, 'regionType': regionType}
        if x==0:
            running += cave[(x,y)]['regionType']
        elif y==0:
            running += cave[(x,y)]['regionType']
        else:
            running = summedCave[(x-1,y)]['value'] + summedCave[(x,y-1)]['value'] - summedCave[(x-1,y-1)]['value'] + cave[(x,y)]['regionType']
        summedCave[(x,y)]={'value': running}
print "grid generated"

# for y in range(800):
#     for x in range(20):
#         if cave[(x,y)]['regionType']==0 or cave[(x,y)]['regionType']==2:
#             print "_",
#         else:
#             print "X",
#     print "\n"

print summedCave[(targetX,targetY)]['value']

def adjacent(pos):
    return [(pos[0]-1,pos[1]), (pos[0]+1, pos[1]), (pos[0],pos[1]-1), (pos[0],pos[1]+1)]

print ("\n")

def find_target(targX,targY):
    item=1 # 0=nothing, 1=torch, 2=gear
    queue = [(0,0,0,item)]
    best_options = {}

    target_set = (targX, targY, 1)
    while len(queue) > 0:
        minutes, x, y, item = heapq.heappop(queue)

        if (x,y,item) == target_set:
            print (minutes, x, y, item)

        if (x,y,item) in best_options and best_options[(x,y,item)] <= minutes:
            continue
        best_options[(x,y,item)] = minutes

        for i in range(3):
            if i != item and i != cave[(x,y)]['regionType']:
                heapq.heappush(queue, (minutes+7, x, y, i))
            
        for option in adjacent((x,y)):
            if option in cave and item != cave[option]['regionType']:
                heapq.heappush(queue, (minutes+1, option[0], option[1], item))

    return best_options[target_set]

y = find_target(targetX, targetY)
print y