t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)

    for i in range(k):
        if a[i] >= b[i]:
            break
    else:
        i = k

    print(sum(a[i:]) + sum(b[:i]))
