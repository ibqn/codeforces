n, k = map(int, input().split())

i = 0
while i < n and 240 - k - 5 * (i + 1) * (i + 2) / 2 >= 0:
    i += 1

print(i)
