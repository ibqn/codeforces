n = int(input())

children = map(int, input().split())

teams = {i: [] for i in range(3)}

for i, c in enumerate(children):
    teams[c - 1].append(i + 1)

teams_num = min(map(len, teams.values()))
print(teams_num)


for t in zip(*teams.values()):
    print(*t)
