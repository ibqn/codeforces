from bisect import bisect_left

n = int(input())

worms = map(int, input().split())

worms_count = [0]

for w in worms:
    worms_count.append(worms_count[-1] + w)

# print(*worms_count)

m = int(input())

juicy = map(int, input().split())

for j in juicy:
    print(bisect_left(worms_count, j))

