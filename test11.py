res = {}
for _ in range(int(input())):
    team1, goal1, team2, goal2 = input().split(';')
    if goal1 == goal2: goal1 = goal2 = 1
    elif goal1 > goal2:
        goal1 = 3
        goal2 = 0
    else:
        goal1 = 0
        goal2 = 3
    if (team1 in res): res[team1].append(goal1)
    else: res[team1] = [goal1]
    if (team2 in res): res[team2].append(goal2)
    else: res[team2] = [goal2]

for team, scores in res.items():
    print(team + ':' + str(len(scores)), scores.count(3), scores.count(1), scores.count(0), sum(scores))