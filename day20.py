import heapq

filename="input/day20input.txt"
file=open(filename,"r")
file=file.readlines()

maze_input=list(file[0][1:-1])

def new_position(position, direction):
    x,y=position
    if direction=='N':
        return (x,y-1)
    if direction=='W':
        return (x-1,y)
    if direction=='E':
        return (x+1,y)
    if direction=='S':
        return (x,y+1)

def add_exits(position,maze,new):
    if position in maze:
        if new not in maze[position]:
            maze[position].append(new)
    else:
        maze[position]=[new]
    if new in maze:
        if position not in maze[new]:
            maze[new].append(position)
    else:
        maze[new]=[position]

#construct maze
maze={}
position=(0,0)
depth=[]
for i in maze_input:
    if i=='N' or i=='E' or i=='S' or i=='W':
        move_to=new_position(position, i)
        add_exits(position,maze,move_to)
        position=move_to
    elif i=='(':
        depth.append(position)
    elif i=='|':
        position=depth[len(depth)-1]
    elif i==')':
        position=depth[len(depth)-1]
        del(depth[len(depth)-1])

def adjacent(x,y):
    return maze[(x,y)]

queue=[(0,0,0)]
best_options={}

while len(queue)>0:
    minutes,x,y = heapq.heappop(queue)

    if (x,y) in best_options and best_options[(x,y)] <= minutes:
        continue
    best_options[(x,y)]=minutes

    for option in adjacent(x,y):
        heapq.heappush(queue, (minutes+1,option[0],option[1]))

highestVal=0
for k,v in best_options.items():
    if v>highestVal:
        highestKey=k
        highestVal=v

print ("Answer for part one: ", highestVal)

count=0
for k,v in best_options.items():
    if v>1000:
        count+=1

print ("Answer for part two: ", count)
