import heapq
import copy
from operator import itemgetter

filename="input/day15input.txt"
file=open(filename,"r")
file=file.readlines()

maxX=len(file[0])
maxY=len(file)

area={}
y=0
maxY=len(file)
for line in file:
    x=0
    line=list(line.strip())
    for cell in line:
        if cell=='#' or cell=='.':
            area[x,y]={'value':cell}
        if cell=='G':
            area[x,y]={'value':'G', 'hitPoints':200, 'moved':False}
        if cell=='E':
            area[x,y]={'value':'E', 'hitPoints':200, 'moved':False}
        x+=1
    y+=1
maxX=len(line)

def exist(symbol):
    for y in range(maxY):
        for x in range(maxX):
            if area[x,y]['value']==symbol:
                return True
    return False

def get_opponent(creature):
    if creature=='G':
        return 'E'
    else:
        return 'G'

def adjacent_opponents(x,y,creature):
    adjacents=[]
    if area[x,y-1]['value']==get_opponent(creature):
        adjacents.append((x,y-1))
    if area[x-1,y]['value']==get_opponent(creature):
        adjacents.append((x-1,y))
    if area[x+1,y]['value']==get_opponent(creature):
        adjacents.append((x+1,y))
    if area[x,y+1]['value']==get_opponent(creature):
        adjacents.append((x,y+1))
    return adjacents

def adjacents(loc,creature):
    x,y=loc
    adjacents=[]
    if area[x,y-1]['value']=='.' or area[x,y-1]['value']==get_opponent(creature):
        adjacents.append((x,y-1))
    if area[x-1,y]['value']=='.' or area[x-1,y]['value']==get_opponent(creature):
        adjacents.append((x-1,y))
    if area[x+1,y]['value']=='.' or area[x+1,y]['value']==get_opponent(creature):
        adjacents.append((x+1,y))
    if area[x,y+1]['value']=='.' or area[x,y+1]['value']==get_opponent(creature):
        adjacents.append((x,y+1))
    return adjacents

def do_a_fight(x,y,creatureType):
    adj_opponents=adjacent_opponents(x,y,creatureType)
    if len(adj_opponents)>0:
        opponents=[]
        for opp in adj_opponents:
            a,b=opp
            opponents.append((a, b, area[opp]['value'], area[opp]['hitPoints'], area[opp]['moved']))
        opponents=sorted(opponents, key=itemgetter(0))
        opponents=sorted(opponents, key=itemgetter(1))
        opponents=sorted(opponents, key=itemgetter(3))
        selected_opponent=opponents[0]
        print ("Creature at location " + str(x) + "," + str(y) + " hits opponent at " + str(selected_opponent[0]) + "," + str(selected_opponent[1]))
        if selected_opponent[3]-3 <= 0:
            area[selected_opponent[0],selected_opponent[1]]={'value':'.'}
        else:
            area[selected_opponent[0],selected_opponent[1]]={'value': selected_opponent[2], 'hitPoints': selected_opponent[3]-3, 'moved': selected_opponent[4]}
        area[x,y]={'value':creatureType, 'hitPoints':area[x,y]['hitPoints'], 'moved':True}

def is_enemy_accessible(x,y,creature):
    visited=[]
    queue = [(x,y)]
    while len(queue) > 0:
        loc = heapq.heappop(queue)
        visited.append(loc)
        if area[loc]['value']==get_opponent(creature):
            return True
        for option in adjacents(loc,creature):
            if option not in visited and option not in queue:
                heapq.heappush (queue, (option))
    return False

turn=1
while exist('G') and exist('E'):
    turn_incomplete=False
    for y in range(maxY):
        for x in range(maxX):
            if (area[x,y]['value']=='G' or area[x,y]['value']=='E') and area[x,y]['moved']==False:
                creatureType=area[x,y]['value']

                adj_opponents=adjacent_opponents(x,y,creatureType)
                if len(adj_opponents)>0:
                    # an opponent is nearby, fighting happens
                    opponents=[]
                    for opp in adj_opponents:
                        a,b=opp
                        opponents.append((a, b, area[opp]['value'], area[opp]['hitPoints'], area[opp]['moved']))
                    opponents=sorted(opponents, key=itemgetter(0))
                    opponents=sorted(opponents, key=itemgetter(1))
                    opponents=sorted(opponents, key=itemgetter(3))
                    selected_opponent=opponents[0]
                    print ("Creature at location " + str(x) + "," + str(y) + " hits opponent at " + str(selected_opponent[0]) + "," + str(selected_opponent[1]))
                    if selected_opponent[3]-3 <= 0:
                        area[selected_opponent[0],selected_opponent[1]]={'value':'.'}
                    else:
                        area[selected_opponent[0],selected_opponent[1]]={'value': selected_opponent[2], 'hitPoints': selected_opponent[3]-3, 'moved': selected_opponent[4]}
                    area[x,y]={'value':creatureType, 'hitPoints':area[x,y]['hitPoints'], 'moved':True}
                else:
                    #no opponents nearby, identify closest enemy
                    if is_enemy_accessible(x,y,creatureType):
                        queue = [(0,(x,y),[])]
                        opponent_distances={}
                        visited=[]
                        dist=0
                        step_max=999
                        while len(queue) > 0:
                            steps,loc,route = heapq.heappop(queue)
                            if steps>dist:
                                dist=steps
                                print ("Searching depth " + str(dist) + " - " + str(len(queue)))
                            if steps > step_max:
                                break
                            a,b=loc
                            visited.append(loc)
                            route=copy.deepcopy(route)
                            if area[a,b]['value']==get_opponent(creatureType):
                                if (a,b) in opponent_distances and steps > opponent_distances[(a,b)]['steps']:
                                    continue
                                elif (a,b) in opponent_distances and steps == opponent_distances[(a,b)]['steps']:
                                    opponent_distances[(a,b)]['routes'].append(route)
                                elif (a,b) in opponent_distances and steps < opponent_distances[(a,b)]['steps']:
                                    opponent_distances[(a,b)]={'steps':steps, 'routes': [route]}
                                else:
                                    opponent_distances[(a,b)]={'steps':steps, 'routes': [route]}
                                    step_max=steps

                            if loc != (x,y):
                                route.append(loc)
                            for option in adjacents(loc,creatureType):
                                if option not in visited:
                                    heapq.heappush (queue, (steps+1, option, route))
                    else:
                        turn_incomplete=True
                        opponent_distances={}
                    if len(opponent_distances) > 0:
                        rearrange=[]
                        for k,v in opponent_distances.items():
                            target=k
                            xpos,ypos=k
                            stepval=v['steps']
                            routes=v['routes']
                            rearrange.append({'x':xpos, 'y':ypos, 'steps': stepval, 'routes':routes})
                        rearrange=sorted(rearrange, key=itemgetter('x'))
                        rearrange=sorted(rearrange, key=itemgetter('y'))
                        rearrange=sorted(rearrange, key=itemgetter('steps'))
                        best=rearrange[0]['routes']
                        first_steps=[]
                        for route in best:
                            if route[0] not in first_steps:
                                first_steps.append(route[0])
                        first_steps=sorted(first_steps, key=itemgetter(0))
                        first_steps=sorted(first_steps, key=itemgetter(1))
                        dest=first_steps[0]

                        print ("Creature at location " + str(x) + "," + str(y) + " moves to " + str(dest) + ", in the direction of " +str(target))
                        hp=area[x,y]['hitPoints']
                        area[x,y]={'value':'.'}
                        area[dest]={'value': creatureType, 'hitPoints':hp, 'moved':True}
                        newx,newy = dest
                        do_a_fight(newx, newy, creatureType)
                    else:
                        print ("Creature at location " + str(x) + "," + str(y) + " could not see a route to an enemy, and didn't move")
    # reset moved
    goblinhp=0
    elfhp=0
    for y in range(maxY):
        for x in range(maxX):
            if 'moved' in area[x,y]:
                area[x,y]['moved']=False
            if area[x,y]['value']=='G':
                goblinhp += area[x,y]['hitPoints']
                print ("G: " + str(area[x,y]['hitPoints']))
            if area[x,y]['value']=='E':
                elfhp += area[x,y]['hitPoints']
                print ("E: " + str(area[x,y]['hitPoints']))
    print ("-- Turn " + str(turn) + " completed. GoblinHP left: " + str(goblinhp) + ", ElfHP left: " + str(elfhp))
    for y in range(maxY):
        for x in range(maxX):
            print (area[x,y]['value'], end="")
        print("")
    
    if goblinhp > elfhp:
        score = goblinhp * turn
        if turn_incomplete:
            score -= goblinhp
    else:
        score = elfhp * turn
        if turn_incomplete:
            score -= elfhp
    turn +=1

print ("Answer to part one: " + str(score))