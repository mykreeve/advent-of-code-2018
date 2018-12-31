import heapq
import copy
import collections
from operator import itemgetter

filename="input/day15input.txt"
file=open(filename,"r")
file=file.readlines()



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

def empty_adjacents(loc):
    x,y=loc
    adjacents=[]
    if area[x+1,y]['value']=='.':
        adjacents.append((x+1,y))
    if area[x,y+1]['value']=='.':
        adjacents.append((x,y+1))
    if area[x,y-1]['value']=='.':
        adjacents.append((x,y-1))
    if area[x-1,y]['value']=='.':
        adjacents.append((x-1,y))
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
        if selected_opponent[3]-3 <= 0 and selected_opponent[2]=='E':
            elves_died=True
            area[selected_opponent[0],selected_opponent[1]]={'value':'.'}
        elif selected_opponent[3]-elf_damage <= 0 and selected_opponent[2]=='G':
            area[selected_opponent[0],selected_opponent[1]]={'value':'.'}
        elif selected_opponent[2]=='E':
            area[selected_opponent[0],selected_opponent[1]]={'value': selected_opponent[2], 'hitPoints': selected_opponent[3]-3, 'moved': selected_opponent[4]}
        elif selected_opponent[2]=='G':
            area[selected_opponent[0],selected_opponent[1]]={'value': selected_opponent[2], 'hitPoints': selected_opponent[3]-elf_damage, 'moved': selected_opponent[4]}                      
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

def desired_squares(creature):
    desired=[]
    for y in range(maxY):
        for x in range(maxX):
            if area[x,y]['value']==get_opponent(creature):
                for a in empty_adjacents((x,y)):
                    desired.append(a)
    desired=sorted(desired, key=itemgetter(0))
    desired=sorted(desired, key=itemgetter(1))
    return desired

elf_damage=3

while True:
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
    turn=1
    elves_died=False
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
                        # print ("Creature at location " + str(x) + "," + str(y) + " hits opponent at " + str(selected_opponent[0]) + "," + str(selected_opponent[1]))
                        if selected_opponent[3]-3 <= 0 and selected_opponent[2]=='E':
                            elves_died=True
                            area[selected_opponent[0],selected_opponent[1]]={'value':'.'}
                        elif selected_opponent[3]-elf_damage <= 0 and selected_opponent[2]=='G':
                            area[selected_opponent[0],selected_opponent[1]]={'value':'.'}
                        elif selected_opponent[2]=='E':
                            area[selected_opponent[0],selected_opponent[1]]={'value': selected_opponent[2], 'hitPoints': selected_opponent[3]-3, 'moved': selected_opponent[4]}
                        elif selected_opponent[2]=='G':
                            area[selected_opponent[0],selected_opponent[1]]={'value': selected_opponent[2], 'hitPoints': selected_opponent[3]-elf_damage, 'moved': selected_opponent[4]}                            
                        area[x,y]={'value':creatureType, 'hitPoints':area[x,y]['hitPoints'], 'moved':True}
                    else:
                        #no opponents nearby, identify closest enemy
                        if is_enemy_accessible(x,y,creatureType):
                            queue = [(0,y,x)]
                            desired=desired_squares(creatureType)
                            meta={(x,y): (0, None)}
                            visited=set()
                            dist=0
                            stop=999
                            while len(queue) > 0:
                                steps,b,a = heapq.heappop(queue)
                                loc = (a,b)
                                if steps > dist:
                                    # print ("Calculating distance " + str(steps) + " - " + str(len(queue)))
                                    dist=steps
                                if loc in desired:
                                    stop=steps
                                if steps==stop+1:
                                    break
                                for option in empty_adjacents(loc):
                                    if option not in meta or meta[option][0] > steps+1:
                                        meta[option]=(steps+1, loc)
                                    if option in visited:
                                        continue
                                    if option not in visited:
                                        if (steps+1, option[1], option[0]) not in queue:
                                            heapq.heappush(queue, (steps+1, option[1], option[0]))
                                visited.add(loc)
        
                            try:   
                                opts=[]
                                for pos, (dist,parent) in meta.items():
                                    if pos in desired:
                                        xpos=pos[0]
                                        ypos=pos[1]
                                        opts.append((xpos, ypos, dist, parent))
                                opts=sorted(opts, key=itemgetter(0))
                                opts=sorted(opts, key=itemgetter(1))
                                opts=sorted(opts, key=itemgetter(2))
                                min_dist = opts[0][2]
                                closest = (opts[0][0], opts[0][1])
                            except ValueError:
                                closest=None

                            target=closest
                            while meta[closest][0] > 1:
                                closest = meta[closest][1]

                        else:
                            turn_incomplete=True
                            closest=None
                        if closest:
                            dest=closest

                            # print ("Creature at location " + str(x) + "," + str(y) + " moves to " + str(dest) + ", in the direction of " +str(target))
                            hp=area[x,y]['hitPoints']
                            area[x,y]={'value':'.'}
                            area[dest]={'value': creatureType, 'hitPoints':hp, 'moved':True}
                            newx,newy = dest
                            do_a_fight(newx, newy, creatureType)
                        else:
                            pass
                            # print ("Creature at location " + str(x) + "," + str(y) + " could not see a route to an enemy, and didn't move")
        # reset moved
        goblinhp=0
        elfhp=0
        for y in range(maxY):
            for x in range(maxX):
                if 'moved' in area[x,y]:
                    area[x,y]['moved']=False
                if area[x,y]['value']=='G':
                    goblinhp += area[x,y]['hitPoints']
                    # print ("G: " + str(area[x,y]['hitPoints']))
                if area[x,y]['value']=='E':
                    elfhp += area[x,y]['hitPoints']
                    # print ("E: " + str(area[x,y]['hitPoints']))
        print ("-- Turn " + str(turn) + " completed. GoblinHP left: " + str(goblinhp) + ", ElfHP left: " + str(elfhp))
        # for y in range(maxY):
        #     for x in range(maxX):
        #         print (area[x,y]['value'], end="")
        #     print("")
        
        if goblinhp > elfhp:
            score = goblinhp * turn
            if turn_incomplete:
                score -= goblinhp
        else:
            score = elfhp * turn
            if turn_incomplete:
                score -= elfhp
        if elf_damage==3:
            part1score=score
        turn +=1
    if elves_died==False:
        break
    print ("=== Completed analysis for elf damage: " + str(elf_damage))
    elf_damage+=1

print ("Answer to part one: " + str(part1score))
print ("Answer to part two: " + str(score))