dq=['3','7','1','0']
first_elf=0
second_elf=1

def end(dq):
    if len(dq)<700000:
        return True
    else:
        position=len(dq)-7
        for n in range(2):
            newList=[]
            for y in range(6):
                newList.append(dq[position+n+y])
            new = int("".join(newList))
            if new==704321:
                print "found it: " + str((position+n))
                return False
        return True

while end(dq):
    newVal = int(dq[first_elf])+int(dq[second_elf])
    if len(str(newVal))>1:
        for n in range(len(str(newVal))):
            dq.append(str(newVal)[n])
    else:
        dq.append(str(newVal))
    first_elf=first_elf+1+int(dq[first_elf])
    while first_elf > len(dq)-1:
        first_elf -= len(dq)
    second_elf=second_elf+1+int(dq[second_elf])
    while second_elf > len(dq)-1:
        second_elf -= len(dq)
    if len(dq)%50000==0:
        print "analysed " + str(len(dq)) + " positions"

print "ten values after position 704321: ", 
for n in range (704321,704331):
    print dq[n],
print ""