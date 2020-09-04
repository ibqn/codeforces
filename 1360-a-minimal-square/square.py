t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    s1 = max(a, 2 * b)
    s2 = max(b, 2 * a)

    s = min(s1, s2)
    print(s ** 2)
