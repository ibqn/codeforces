_ = int(input())  # n is not needed

groups = list(map(int, input().split()))

counts = {c: groups.count(c) for c in range(1, 5)}

# print(counts)
counts[1] = max(0, counts[1] - counts[3])
counts[1] = max(0, counts[1] - 2 * (counts[2] % 2))
counts[1] = (counts[1] + 3) // 4
counts[2] = (counts[2] + 1) // 2  # same as counts[2] // 2 + counts[2] % 2
# print(counts)

print(sum(counts.values()))
