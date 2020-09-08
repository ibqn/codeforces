t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    i = n - 2
    j = n - 1
    l = False
    r = False

    while i >= 0:
        l = a[i] > 0 and i < j
        if not l:
            i -= 1

        r = a[j] < 0
        if not r:
            j -= 1

        if l and r:
            v = min(a[i], -a[j])
            a[i] -= v
            a[j] += v

    # print(*a)

    answer = sum(v for v in a if v > 0)
    print(answer)

