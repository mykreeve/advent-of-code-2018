nanos = []
from z3 import *

filename="input/day23input.txt"
file=open(filename,"r")
for line in file:
    l = line.strip().split(",")
    x = int(l[0][5:])
    y = int(l[1])
    z = int(l[2][:-1])
    r = int(l[3][3:])
    nanos.append((x,y,z,r))

biggest_x=0
lowest_x=0
biggest_y=0
lowest_y=0
biggest_z=0
lowest_z=0
biggest_range=0
for n in nanos:
    if n[3] > biggest_range:
        best_nano = n
        biggest_range = n[3]
    if n[0] > biggest_x:
        biggest_x = n[0]
    if n[1] > biggest_y:
        biggest_y = n[1]
    if n[2] > biggest_z:
        biggest_z = n[2]
    if n[0] < lowest_x:
        lowest_x = n[0]
    if n[1] < lowest_y:
        lowest_y = n[1]
    if n[2] < lowest_z:
        lowest_z = n[2]

print ("x: ", str(lowest_x), " to ", str(biggest_x))
print ("y: ", str(lowest_y), " to ", str(biggest_y))
print ("z: ", str(lowest_z), " to ", str(biggest_z))

contactable=0
uncontactable=0
for n in nanos:
    dist = abs(n[0]-best_nano[0]) + abs(n[1]-best_nano[1]) + abs(n[2]-best_nano[2])
    if dist < best_nano[3]:
        contactable += 1
    else:
        uncontactable += 1

print (best_nano)
print (contactable)

def z3_abs(x):
    return If(x >= 0,x,-x)

def z3_dist(x, y):
    return z3_abs(x[0] - y[0]) + z3_abs(x[1] - y[1]) + z3_abs(x[2] - y[2])

data = [(x[3], tuple(x[:-1])) for x in nanos]

x = Int('x')
y = Int('y')
z = Int('z')
orig = (x, y, z)
cost_expr = x * 0
for r, pos in data:
    cost_expr += If(z3_dist(orig, pos) <= r, 1, 0)
opt = Optimize()
print("let's go")
opt.maximize(cost_expr)
opt.minimize(z3_dist((0,0,0), (x, y, z)))

opt.check()

model = opt.model()
print(model)
# print(dist((0,0,0), (model[x], model[y], model[z])))

x=11723885
y=42181850
z=29873299
contactable=0
for n in nanos:
    dist = abs(n[0]-x) + abs(n[1]-y) + abs(n[2]-z)
    if dist < n[3]:
        contactable +=1
print (contactable)

# biggest_x=0
# lowest_x=9999999999999999
# biggest_y=0
# lowest_y=9999999999999999
# biggest_z=0
# lowest_z=9999999999999999
# biggest_range=0
# most_contactable=0
# best_dist=9999999999999999999
# for x in range(10700000, 83779034, 2000):
#     for y in range(0, 83779034-x, 2000):
#         z=83779034-x-y
# # for x in range(11723883, 11723886, 1):
# #     print ("testing " + str(x))
# #     for y in range(42181848, 42181852, 1):
# #         for z in range (29873295, 29873299, 1):
#         if (x+y+z)==83779034:
#             contactable=0
#             for n in nanos:
#                 dist = abs(n[0]-x) + abs(n[1]-y) + abs(n[2]-z)
#                 if dist < n[3]:
#                     contactable +=1
#             if contactable >= most_contactable:
#                 most_contactable = contactable
#                 print (x,y,z,contactable, (x+y+z))
#             # if contactable>=798:
#             #     zero_dist = x+y+z
#             #     if zero_dist < best_dist:
#             #         print ("\n")
#             #         print ("x: " + str(x) + " y: " + str(y) + " z: " + str(z) + " dist: " + str(zero_dist) + " contact: " + str(contactable))
#             #         best_dist=zero_dist
