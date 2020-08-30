t = int(input())

for _ in range(t):
    n = int(input())

    a = sorted(set(map(int, input().split())))

    if (a[0] + len(a) - 1) == a[-1]:
        print("YES")
    else:
        print("NO")

