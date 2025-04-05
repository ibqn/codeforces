n = int(input())


def prefix_sum():
    an = int(input())
    a = list(map(int, input().split()))

    pa = []
    s = 0
    for i in range(an):
        s += a[i]
        pa.append(s)

    return pa


for _ in range(n):
    pa = prefix_sum()
    pb = prefix_sum()

    print(max(0, max(pa) + max(pb)))
