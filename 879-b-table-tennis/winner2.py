n, k = map(int, input().split())

powers = list(map(int, input().split()))

power = powers[0]
wins = 0

for i in range(1, n):
    if power > powers[i]:
        wins += 1
    else:
        wins = 1
        power = powers[i]

    if wins >= k:
        break

print(power)
