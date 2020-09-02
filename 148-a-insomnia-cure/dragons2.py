nums = [int(input()) for _ in range(4)]

n = int(input())

result = 0

for d in range(1, n + 1):
    if any([d % i == 0 for i in nums]):
        result += 1

print(result)
