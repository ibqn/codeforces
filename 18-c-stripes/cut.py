n = int(input())

stripe = list(map(int, input().split()))

count = 0

left = 0
right = sum(stripe)

for s in stripe[:-1]:
    left += s
    right -= s

    if left == right:
        count += 1

print(count)
