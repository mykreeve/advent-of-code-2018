from operator import itemgetter

filename="input/day13input.txt"
file=open(filename,"r")
layout=[]
carts=[]
cartno=1
turn=1

def add_cart (direction,y,x,cartno):
    carts.append({'direction': direction, 'x': x, 'y': y, 'turn': 'left', 'cart':cartno})

def crash_resolution():
    for n,cart in enumerate(carts):
        for n2,cart2 in enumerate(carts):
            if cart['x']==cart2['x'] and cart['y']==cart2['y'] and n != n2:
                # print "There has been a crash at: " + str(cart['x']) + ", " + str(cart['y']) + " -- " + str(turn)
                cart['delete']=1
                cart2['delete']=1

def delete_carts():
    deleteArray=[]
    for n,cart in enumerate(carts):
        if 'delete' in cart:
            deleteArray.append(cart)
    for d in deleteArray:
        carts.remove(d)

for line in file:
    line = line.strip('\n')
    lineArray=[]
    for item in line:
        lineArray.append(item)
    layout.append(lineArray)
for y,line in enumerate(layout):
    for x,item in enumerate(line):
        if item=="^":
            print "cart going up: " + str(x) + ", " + str(y)
            add_cart('up',y,x,cartno)
            cartno += 1
            layout[y][x]="|"
        if item==">":
            print "cart going right: " + str(x) + ", " + str(y)
            add_cart('right',y,x,cartno)
            cartno += 1
            layout[y][x]="-"
        if item=="<":
            print "cart going left: " + str(x) + ", " + str(y)
            add_cart('left',y,x,cartno)
            cartno += 1
            layout[y][x]="-"
        if item=="v":
            print "cart going down: " + str(x) + ", " + str(y)
            add_cart('down',y,x,cartno)
            cartno += 1
            layout[y][x]="|"

def move_cart(n, cart):
    if cart['direction']=='up':
        cart['y'] -= 1
        if layout[cart['y']][cart['x']] == '/':
            cart['direction']='right'
        if layout[cart['y']][cart['x']] == '\\':
            cart['direction']='left'
        if layout[cart['y']][cart['x']] == '+':
            if cart['turn']=='left':
                cart['direction']='left'
                cart['turn']='straight'
            elif cart['turn']=='straight':
                cart['turn']='right'
            elif cart['turn']=='right':
                cart['direction']='right'
                cart['turn']='left'
    elif cart['direction']=='left':
        cart['x'] -= 1
        if layout[cart['y']][cart['x']] == '/':
            cart['direction']='down'
        if layout[cart['y']][cart['x']] == '\\':
            cart['direction']='up'
        if layout[cart['y']][cart['x']] == '+':
            if cart['turn']=='left':
                cart['direction']='down'
                cart['turn']='straight'
            elif cart['turn']=='straight':
                cart['turn']='right'
            elif cart['turn']=='right':
                cart['direction']='up'
                cart['turn']='left'
    elif cart['direction']=='down':
        cart['y'] += 1
        if layout[cart['y']][cart['x']] == '/':
            cart['direction']='left'
        if layout[cart['y']][cart['x']] == '\\':
            cart['direction']='right'
        if layout[cart['y']][cart['x']] == '+':
            if cart['turn']=='left':
                cart['direction']='right'
                cart['turn']='straight'
            elif cart['turn']=='straight':
                cart['turn']='right'
            elif cart['turn']=='right':
                cart['direction']='left'
                cart['turn']='left'
    elif cart['direction']=='right':
        cart['x'] += 1
        if layout[cart['y']][cart['x']] == '/':
            cart['direction']='up'
        if layout[cart['y']][cart['x']] == '\\':
            cart['direction']='down'
        if layout[cart['y']][cart['x']] == '+':
            if cart['turn']=='left':
                cart['direction']='up'
                cart['turn']='straight'
            elif cart['turn']=='straight':
                cart['turn']='right'
            elif cart['turn']=='right':
                cart['direction']='down'
                cart['turn']='left'

def more_than_one_cart():
    if len(carts) > 1:
        return True
    return False

while more_than_one_cart():
    carts=sorted(carts, key=itemgetter('x'))
    carts=sorted(carts, key=itemgetter('y'))
    for n,cart in enumerate(carts):
        move_cart(n,cart)
        crash_resolution()
    delete_carts()
    # print str(turn) + ": ",
    # for i in carts:
    #         print str(i['x']) + ',' + str(i['y']) + " ("+str(i['cart'])+")",
    # print "\n"
    if len(carts)==1:
        print carts[0]['x'], carts[0]['y']
    turn += 1

