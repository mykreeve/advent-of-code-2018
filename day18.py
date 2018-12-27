import copy

filename="input/day18input.txt"
file=open(filename,"r")
file=file.readlines()

grid=[]
for line in file:
    line=line.strip()
    grid.append(list(line))

def get_adjacent(y,x,grid):
    borders=[]
    if (x-1) >= 0:
        borders.append(grid[y][x-1])
        if (y-1) >= 0:
            borders.append(grid[y-1][x-1])
        if (y+1) <= len(grid[y])-1:
            borders.append(grid[y+1][x-1])
    if (x+1) <= len(grid[y])-1:
        borders.append(grid[y][x+1])
        if (y-1) >= 0:
            borders.append(grid[y-1][x+1])
        if (y+1) <= len(grid[y])-1:
            borders.append(grid[y+1][x+1])
    if (y-1) >= 0:
        borders.append(grid[y-1][x])
    if (y+1) <= len(grid)-1:
        borders.append(grid[y+1][x])
    return borders

def count(objs, item):
    a=0
    for i in objs:
        if i==item:
            a+=1
    return a

def grid_count(grid, item):
    a=0
    for line in grid:
        for i in line:
            if i==item:
                a+=1
    return a

def do_print(grid):
    for y in grid:
        print ("".join(y))
    print ("\n")

time=0
counters=[]
while time < 650:
    new_grid=copy.deepcopy(grid)
    for ypos,row in enumerate(grid):
        for xpos,chara in enumerate(row):
            adj = get_adjacent(ypos,xpos,grid)
            trees = count(adj, '|')
            lumbers = count(adj, '#')
            if chara=='.' and trees >= 3:
                new_grid[ypos][xpos]='|'
            if chara=='|' and lumbers>=3:
                new_grid[ypos][xpos]='#'
            if chara=='#':
                if lumbers<1 or trees<1:
                    new_grid[ypos][xpos]='.'
            # print (adj, str(ypos), str(xpos), str(trees))
    grid = copy.deepcopy(new_grid)
    time += 1
    counters.append({ 'trees': grid_count(grid,'|'), 'lumberyards': grid_count(grid,'#') })


print ("Answer to part one: " + str(counters[9]['trees'] * counters[9]['lumberyards']))

# Once the system has been running for 453 minutes, it repeats on a 28 minute cycle, so to find
# status after that, just take required number of minutes and keep removing 28 until a known value results
required=1000000000
while required>649:
    required=required-28
print ("Answer to part two: " + str(counters[required-1]['trees'] * counters[required-1]['lumberyards']) )

