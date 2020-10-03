t = int(input())

for _ in range(t):
    n = int(input())
    ais = list(map(int, input().split()))
    bis = list(map(int, input().split()))

    mina = min(ais)
    minb = min(bis)

    count = 0

    for a, b in zip(ais, bis):
        count += max(a - mina, b - minb)

    print(count)
