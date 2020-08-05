n, m, k = list(map(int, input().split()))

roads = [list(map(int, input().split())) for _ in range(m)]

storages = set(map(int, input().split())) if k > 0 else set()

costs = set(w for (c1, c2, w) in roads if (c1 in storages) != (c2 in storages))

print(min(costs) if costs else -1)
