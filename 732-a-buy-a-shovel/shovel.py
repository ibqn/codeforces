k, r = map(int, input().split())

k = int(str(k)[-1])

idx = (
    [False] + [(k * i) % 10 == r or (k * i) % 10 == 0 for i in range(1, 10)] + [True]
).index(True)

print(idx)
