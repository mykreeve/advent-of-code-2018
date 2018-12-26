def reaction_exist(mol):
        for a in range(len(mol)):
                if mol[a].isupper():
                        if mol[a+1].islower():
                                if mol[a].upper() == mol[a+1].upper():
                                        return True
                if mol[a].islower():
                        if mol[a+1].isupper():
                                if mol[a].upper() == mol[a+1].upper():
                                        return True
        return False


filename="input/day5input.txt"
file=open(filename,"r")
molecule=file.readlines()[0]
molecule=list(molecule)
while reaction_exist(molecule):
	print len(molecule)
	for a in range(len(molecule)):
		if molecule[a].isupper():
                        if molecule[a+1].islower():
                                if molecule[a].upper() == molecule[a+1].upper():
                                        del(molecule[a])
					del(molecule[a])
					break
                if molecule[a].islower():
                        if molecule[a+1].isupper():
                                if molecule[a].upper() == molecule[a+1].upper():
					del(molecule[a])
					del(molecule[a])
					break
print len(molecule)-1

