import re
from operator import itemgetter
import math

filename="input/day24input.txt"
file=open(filename,"r")
file=file.readlines()

victory=0
immune_boost=1

while victory==0:
    groups=[]
    id=0
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
        if team_to_add_to=='Immune System':
            damage += immune_boost
        damageType=dam[1]
        init=proc[1].split(' ')
        initiative=int(init[1])


        item={ 'id': id,
        'team': team_to_add_to,
        'units': units,
        'hitPoints': hitPoints,
        'weakTo': weakTo,
        'immuneTo': immuneTo,
        'initiative': initiative,
        'damage': damage,
        'damageType': damageType}
        groups.append(item)
        id += 1

    def exists(team):
        for i in groups:
            if i['team']==team:
                return True
        return False

    def other_team(team):
        if team=='Immune System':
            return 'Infection'
        else:
            return 'Immune System'

    def determine_group_to_attack(damage, groups):
        values=[]
        for i,n in enumerate(damage):
            values.append((groups[i]['id'], n, groups[i]['effectivePower'], groups[i]['initiative']))
        values=sorted(values, key=itemgetter(3), reverse=True)
        values=sorted(values, key=itemgetter(2), reverse=True)
        values=sorted(values, key=itemgetter(1), reverse=True)
        if values[0][1]==0:
            return (0, -1)
        else:
            return (values[0][1], values[0][0])

    getOut=0
    while exists('Immune System') and exists('Infection') and getOut==0:
        # Targetting
        for n,i in enumerate(groups):
            i['effectivePower']=i['units']*i['damage']
        groups=sorted(groups, key=itemgetter('effectivePower'), reverse=True)
        for i in groups:
            damage=[]
            for opponent in groups:
                multiplier=1
                if i['id']==opponent['id']:
                    damage.append(0)
                    continue
                if opponent['team']!= other_team(i['team']):
                    damage.append(0)
                    continue
                if i['damageType'] in opponent['immuneTo']:
                    damage.append(0)
                    continue
                if 'targettedBy' in opponent and opponent['targettedBy']>=0:
                    damage.append(0)
                    continue
                if i['damageType'] in opponent['weakTo']:
                    multiplier=2
                damage.append(i['effectivePower']*multiplier)
            doing, target = determine_group_to_attack(damage, groups)
            if target >= 0:
                i['targetting']=target
                for iter in groups:
                    if iter['id']==target:
                        iter['targettedBy']=i['id']
        # resolve damage (attack phase)
        groups=sorted(groups, key=itemgetter('initiative'), reverse=True)

        hits=0
        for l in groups:
            if l['targetting']>-1:
                hits += 1
                targ=l['targetting']
                for target in groups:
                    if target['id']==targ:
                        damageInRound=l['damage']*l['units']
                        if l['damageType'] in target['weakTo']:
                            damageInRound=damageInRound*2
                        l['damageInRound']=damageInRound
                        kills = math.floor(float(l['damageInRound'])/float(target['hitPoints']))
                        if kills==0:
                            hits -= 1
                        target['units']=target['units']-kills
                        if target['units']<0:
                            target['units']=0
        if hits==0:
            getOut=1

        # remove dead groups
        temp_groups=[]
        for l in groups:
            if l['units']!=0:
                temp_groups.append(l)
        groups = temp_groups

        # remove targetting
        for group in groups:
            group['targetting']=-1
            group['targettedBy']=-1
            group['damageInRound']=0

        # print (groups)

    print ("Immune Boost: " + str(immune_boost))
    if (exists('Immune System') and exists('Infection')):
        print ("Stalemate")
    else:
        print (groups[0]['team'] + " wins")
    tot=0
    for group in groups:
        tot += group['units']
    print (tot)
    if groups[0]['team']=='Immune System':
        victory=1
    immune_boost += 1