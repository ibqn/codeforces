t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    odd = sum(map(lambda v: int(int(v) % 2 != 0), input().split()))

    even = n - odd
    cor = int(odd % 2 == 0) + int(even % 2 == 0 and x % 2 == 0)

    if odd > 0 and n - cor >= x and not (even == 0 and x % 2 == 0):
        print("YES")
    else:
        print("NO")

