n, length = map(int, input().split())

positions = list(map(int, input().split()))
positions.sort()

# print(*positions)

radii = [(positions[i] - positions[i - 1]) / 2 for i in range(1, n)]
radii += [positions[0], length - positions[-1]]

print(max(radii))

