import re

filename="input/day24input.txt"
file=open(filename,"r")
file=file.readlines()

groups=[]
team_to_add_to='Immune System'

for line in file:
    weakTo=[]
    immuneTo=[]
    if re.match("^Immune.+", line):
        team_to_add_to='Immune System'
        continue
    if re.match("^Infection.+", line):
        team_to_add_to='Infection'
        continue
    if re.match("^$", line):
        continue
    proc=line.strip().split(' units')
    units=int(proc[0])
    proc=proc[1]
    proc=proc[11:].split(' hit points')
    hitPoints=int(proc[0])
    proc=proc[1]
    if re.match(".+weak to.+", proc) or re.match(".+immune to.+", proc):
        proc=proc.split(') ')
        special=proc[0].strip(' (').replace(' to',',').replace('; ', ', ').split(', ')
        for i in special:
            if i=='weak':
                addTo=weakTo
                continue
            if i=='immune':
                addTo=immuneTo
                continue
            addTo.append(i)
        proc=proc[1]
    proc=proc.strip('with an attack that does ').replace(' damage at', ',').split(', ')
    dam=proc[0].split(' ')
    damage=int(dam[0])
    damageType=dam[1]
    init=proc[1].split(' ')
    initiative=int(init[1])


    item={ 'team': team_to_add_to,
    'units': units,
    'hitPoints': hitPoints,
    'weakTo': weakTo,
    'immuneTo': immuneTo,
    'initiative': initiative,
    'damage': damage,
    'damageType': damageType}
    groups.append(item)

print(groups)
