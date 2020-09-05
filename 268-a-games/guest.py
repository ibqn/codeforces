n = int(input())

teams = []
pairs = {}
for _ in range(n):
    h, a = map(int, input().split())

    teams.append(h)
    pairs[a] = pairs.get(a, 0) + 1

count = 0
for t in teams:
    count += pairs.get(t, 0)

print(count)

