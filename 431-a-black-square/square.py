calories = list(map(int, input().split()))
data = [int(c) - 1 for c in input()]

wastes = {}
for c in data:
    wastes[c] = wastes.get(c, 0) + 1

answer = sum(calories[i] * wastes.get(i, 0) for i in range(4))
print(answer)
