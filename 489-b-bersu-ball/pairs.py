n = int(input())
boys = sorted(list(map(int, input().split())))

m = int(input())
girls = sorted(list(map(int, input().split())))

# print(*boys)
# print(*girls)

count = 0
b, g = 0, 0
while b < n and g < m:
    diff = boys[b] - girls[g]
    if abs(diff) <= 1:
        b += 1
        g += 1
        count += 1
    elif diff > 0:
        g += 1
    else:
        b += 1

print(count)

