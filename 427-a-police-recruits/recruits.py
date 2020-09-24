n = int(input())

events = map(int, input().split())

recruits = 0
crimes = 0
for e in events:
    recruits += e
    if recruits < 0:
        recruits = 0
        crimes += 1

print(crimes)
