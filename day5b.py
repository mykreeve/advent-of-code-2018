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

def letter_exist(mol,alpha):
	for a in range(len(mol)):
		if mol[a].lower() == alpha:
			return True
	return False

alpha = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alpha)

for b in range(len(alphabet)):
	filename="day5input.txt"
	file=open(filename,"r")
	molecule=file.readlines()[0]
	molecule=list(molecule)
	execs=0
	while letter_exist(molecule, alphabet[b]):
		for a in range(len(molecule)):
			if molecule[a].lower() == alphabet[b]:
				del(molecule[a])
				break
	print str(alphabet[b]) + " stripped from string, " + str(len(molecule)) + " letters remain"
	while reaction_exist(molecule):
		for a in range(len(molecule)):
			if molecule[a].isupper():
                        	if molecule[a+1].islower():
                                	if molecule[a].upper() == molecule[a+1].upper():
                                        	del(molecule[a])
						del(molecule[a])
						execs += 1
						break
                	if molecule[a].islower():
                        	if molecule[a+1].isupper():
                                	if molecule[a].upper() == molecule[a+1].upper():
						del(molecule[a])
						del(molecule[a])
						execs += 1
						break
	print str(alphabet[b]) + " removed from molecule,  " + str(execs) + " reactions occurred, leaving molecule of length: " + str(len(molecule)-1)
	file.close()

