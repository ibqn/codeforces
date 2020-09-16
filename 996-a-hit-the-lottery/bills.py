n = int(input())

bills = [100, 20, 10, 5]

count = 0

for b in bills:
    val, rest = divmod(n, b)
    count += val
    if not rest:
        break
    n = rest
else:
    count += rest

print(count)
