t = int(input())

for _ in range(t):
    n = int(input())

    l = n // 2
    if l % 2 != 0:
        print("NO")
        continue

    even = [2 * (i + 1) for i in range(l)]
    odd = [1 + 2 * i for i in range(l - 1)]
    result = even + odd + [sum(even) - sum(odd)]

    print("YES")
    print(*result)
