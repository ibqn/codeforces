from itertools import accumulate


n = int(input())


def prefix_sum():
    an = int(input())
    a = map(int, input().split())

    # pa = [0]
    # s = 0
    # for i in range(an):
    #     s += a[i]
    #     pa.append(s)

    # return pa
    return accumulate(a, initial=0)


for _ in range(n):
    pa = prefix_sum()
    pb = prefix_sum()

    print(max(pa) + max(pb))
