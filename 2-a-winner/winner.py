from itertools import takewhile

n = int(input())

players = {}

for i in range(n):
    name, points = input().split()

    data = players.get(name, {'score': 0, 'points': []})
    data['score'] += int(points)
    data['points'].append((data['score'], i + 1))

    players[name] = data

winners = sorted(players.items(), key=lambda item: item[1]['score'], reverse=True)

top = winners[0]

top_shared = [p for p in takewhile(lambda p: p[1]['score'] == top[1]['score'], winners)]

top_list = []
for top in top_shared:
    name, hist = top
    min_round = min([ p[1] for p in hist['points'] if p[0] >= hist['score'] ])
    top_list.append((name, min_round))

winner = sorted(top_list, key=lambda item: item[1]).pop(0)
print(winner[0])






