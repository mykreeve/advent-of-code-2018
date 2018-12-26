players=459
max_marble_no=7179000
player_scores={}
current_player=1
marble_no=1
circle=[0]
current_position=0

def add_player_score(player, score):
    if player in player_scores:
        player_scores[player] += score
    else:
        player_scores[player] = score

while marble_no<max_marble_no:
    if marble_no%23==0:
        add_player_score(current_player, marble_no)
        current_position = current_position - 7
        if current_position<0:
            current_position=current_position+len(circle)
        add_player_score(current_player, circle[current_position])
        del circle[current_position]

    else:
        position_to_add=(current_position+2)%len(circle)
        if position_to_add==0:
            circle.append(marble_no)
            current_position=len(circle)-1
        else:
            circle.insert(position_to_add, marble_no)
            current_position=position_to_add
    marble_no += 1
    current_player += 1
    if current_player>players:
        current_player=1
    if marble_no%1000==0:
        print str(marble_no), "/", str(max_marble_no)

highest_score=0
best_player=0
for k,v in player_scores.iteritems():
    if v>highest_score:
        best_player=k
        highest_score=v
print best_player, highest_score