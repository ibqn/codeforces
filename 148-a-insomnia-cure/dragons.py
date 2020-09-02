nums = [int(input()) for _ in range(4)]

n = int(input()) + 1
dragons = [0] * n

for i in nums:
    for d in range(0, n, i):
        dragons[d] = 1

print(sum(dragons) - 1)
