stars = []
stars_done = []
constellations = []

filename="input/day25input.txt"
file=open(filename,"r")
for line in file:
    x=line.strip("\n").split(",")
    stars.append([int(x[0]), int(x[1]), int(x[2]), int(x[3])])
    stars_done.append(False)

def is_proximate(star,candidate):
    distance = abs(star[0]-candidate[0]) + abs(star[1]-candidate[1]) + abs(star[2]-candidate[2]) + abs(star[3]-candidate[3])
    if distance <= 3:
        return True
    return False

def candidates_remain(new):
    for star_pos in new:
        examine = stars[star_pos]
        for no, star in enumerate(stars):
            if stars_done[no]==False and is_proximate(star, examine):
                return True
    return False

for pos,star in enumerate(stars):
    if stars_done[pos]==False:
        new_constellation=[]
        new_constellation.append(pos)
        stars_done[pos]=True
        evaluate_star = star
        for cand_pos, cand_star in enumerate(stars):
            if cand_pos != pos and is_proximate(star,cand_star):
                new_constellation.append(cand_pos)
                stars_done[cand_pos]=True
        while candidates_remain(new_constellation):
            for star_pos in new_constellation:
                examine = stars[star_pos]
                for no, star in enumerate(stars):
                    if stars_done[no]==False and is_proximate(star, examine):
                        new_constellation.append(no)
                        stars_done[no]=True
        constellations.append(new_constellation)

print (constellations)
print (len(constellations))
