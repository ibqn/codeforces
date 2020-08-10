_ = int(input())  # n is not needed

counts = {k: 0 for k in range(1, 5)}

groups = list(map(int, input().split()))

for g in groups:
    counts[g] = counts.get(g, 0) + 1

# print(counts)
counts[1] = max(0, counts[1] - counts[3])
counts[1] = max(0, counts[1] - 2 * (counts[2] % 2))
counts[1] = (counts[1] + 3) // 4
counts[2] = (counts[2] + 1) // 2  # same as counts[2] // 2 + counts[2] % 2
# print(counts)

print(sum(counts.values()))
