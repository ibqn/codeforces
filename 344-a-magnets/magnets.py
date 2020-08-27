n = int(input())

groups = 1
magnet = input()

for _ in range(1, n):
    m = input()
    if magnet != m:
        groups += 1
        magnet = m

print(groups)
