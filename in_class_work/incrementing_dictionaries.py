
team_scores = {"team 1" : 10,
               "team 2" : 15}

team_scores["team 1"] += 17
print(team_scores)

# team_scores["team 3"] += 13 <---this doesn't work because team 3 isn't a key
# print(team_scores)

team_scores["team 3"] = 13
print(team_scores)

team_name = "team 85"
team_score = 11


if team_name in team_scores.keys():
    #if this key exists, increment
    team_scores[team_name] += team_score 
else: 
    # if not, add the entry 
    team_scores[team_name] = team_score

#########################################################

# 0. make a function
# 1. figure out what you want to get out of this function (return) 
# 2. figure out what you want to give as input (arguments)
# 3. figure out how to go fro arguments to return
# 4. test it!
# 5. write a helpful docstring 

def increment_teamscores(score_dict, name, score,):

    """
    function takes scores dictionary, and the name and score of a team, and will either increment 
    that team's score or add it as a new team.
    """
    if name in score_dict.keys():
    #if this key exists, increment
        score_dict[name] += score 
    else: 
    # if not, add the entry 
        score_dict[name] = score
    #we want to end up with an updated dictionary but since dicts are mutable, we don't need to explicitly return it
    return None    

team_scores = {"team 1" : 10, 
               "team 2" : 15}
increment_teamscores(team_scores, "team 13", 29)
print(team_score)

########### run some examples

all_team_scores = { "Team Alpha" : 10, 
                   "Team Gamma" : 17}

increment_teamscores(all_team_scores, "Team Strike Force", 84)
increment_teamscores(all_team_scores, "Team Discovery Channel", 13)
increment_teamscores(all_team_scores, "Team Discovery Channel", 44)
increment_teamscores(all_team_scores, "Team Alpha", 17)

print(all_team_scores)
