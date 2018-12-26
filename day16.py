import re
import copy

filename="input/day16input.txt"
file=open(filename,"r")
file=file.readlines()

tests=0
for line in file:
    if re.match("^Before.+", line):
        tests += 1

inputs=[]
commands=[]
outputs=[]
programme=[]

for i in range(tests):
    line = file[(i*4)].strip().split(",")
    input=[]
    input.append(int(line[0][9:]))
    input.append(int(line[1]))
    input.append(int(line[2]))
    input.append(int(line[3][1]))
    inputs.append(input)

for c in range(tests):
    line = file[(c*4)+1].strip().split(" ")
    commands.append([int(line[0]), int(line[1]), int(line[2]), int(line[3])])

for o in range(tests):
    line = file[(o*4)+2].strip().split(",")
    output=[]
    output.append(int(line[0][9:]))
    output.append(int(line[1]))
    output.append(int(line[2]))
    output.append(int(line[3][1]))
    outputs.append(output)

for p in range((tests*4)+2, len(file)):
    line = file[p].strip().split(" ")
    programme.append([int(line[0]), int(line[1]), int(line[2]), int(line[3])])


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

investigates=[]
for i in range(len(inputs)):
    inp = copy.deepcopy(inputs[i])
    successes=[]
    for f in functions:
        tinp = copy.deepcopy(inp)
        test_output=f(tinp, commands[i][1], commands[i][2], commands[i][3])
        if test_output==outputs[i]:
            successes.append(f.__name__)
    investigates.append({'command_ref': commands[i][0], 'possibilities': successes})

zoop=0
for i in investigates:
    if len(i['possibilities']) >= 3:
        zoop += 1

print ("Answer to part 1: " + str(zoop))

working_investigates = copy.deepcopy(investigates)
determination=[]
while len(determination) < len(functions):
    for i in working_investigates:
        if (len(i['possibilities'])) == 1:
            id = i['possibilities'][0]
            determination.append({'command_ref': i['command_ref'], 'meaning': id})
            for j in working_investigates:
                if id in j['possibilities']:
                    j['possibilities'].remove(id)


def get_function(name):
    for f in functions:
        if f.__name__ == name:
            return f

ordered_functions=[]
for i in range(len(functions)):
    for l in determination:
        if l['command_ref']==i:
            j = get_function(l['meaning'])
            ordered_functions.append(j)

register = [0,0,0,0]
for command in programme:
    register = ordered_functions[command[0]](register, command[1], command[2], command[3])
print ("final output: " + str(register))
print ("Answer to part 2: " + str(register[0]))