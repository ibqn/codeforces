n = int(input())

pts = list(map(int, input().split()))

min_pts = pts[0]
max_pts = pts[0]
count = 0

for p in pts[1:]:
    if min_pts > p:
        min_pts = p
        count += 1
    elif max_pts < p:
        max_pts = p
        count += 1

print(count)
