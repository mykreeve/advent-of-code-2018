import copy

def addr(register,a,b,c):
    register[c]=register[a]+register[b]
    return register
def addi(register,a,b,c):
    register[c]=register[a]+b
    return register
def mulr(register,a,b,c):
    register[c]=register[a]*register[b]
    return register
def muli(register,a,b,c):
    register[c]=register[a]*b
    return register
def banr(register,a,b,c):
    register[c]=register[a]&register[b]
    return register
def bani(register,a,b,c):
    register[c]=register[a]&b
    return register
def borr(register,a,b,c):
    register[c]=register[a]|register[b]
    return register
def bori(register,a,b,c):
    register[c]=register[a]|b
    return register
def setr(register,a,b,c):
    register[c]=int(register[a])
    return register
def seti(register,a,b,c):
    register[c]=int(a)
    return register
def gtir(register,a,b,c):
    if a > register[b]:
        register[c]=1
    else:
        register[c]=0
    return register
def gtri(register,a,b,c):
    if register[a] > b:
        register[c]=1
    else:
        register[c]=0
    return register
def gtrr(register,a,b,c):
    if register[a] > register[b]:
        register[c]=1
    else:
        register[c]=0
    return register
def eqir(register,a,b,c):
    if a == register[b]:
        register[c]=1
    else:
        register[c]=0
    return register
def eqri(register,a,b,c):
    if register[a] == b:
        register[c]=1
    else:
        register[c]=0
    return register
def eqrr(register,a,b,c):
    if register[a] == register[b]:
        register[c]=1
    else:
        register[c]=0
    return register

functions=[addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def get_function(name):
    for f in functions:
        if f.__name__ == name:
            return f

filename="input/day19input.txt"
file=open(filename,"r")
file=file.readlines()

ip=int(file[0].strip().split(" ")[1])

programme=[]
for l in range(1, len(file)):
    trans = (file[l].strip().split(" "))
    programme.append([trans[0], int(trans[1]), int(trans[2]), int(trans[3])])

register=[0,0,0,0,0,0]

while register[3]<len(programme):
    ip=register[3]
    register = get_function(programme[ip][0])(register, programme[ip][1], programme[ip][2], programme[ip][3])
    register[3] += 1

register[3] -= 1
print ("\n")
print ("Answer to part 1: " + str(register[0]))

tot=[]
for i in range(1, 10551341):
    if float(10551340)/float(i) == int(float(10551340)/float(i)):
        tot.append(i)
print ("Answer to part 2: " + str(sum(tot)))

# goes=0
# while register[3]<len(programme):
#     ip=register[3]
#     register = get_function(programme[ip][0])(register, programme[ip][1], programme[ip][2], programme[ip][3])

# register[3] -= 1
# print ("\n")
# print ("Answer to part 2: " + str(register[0]))