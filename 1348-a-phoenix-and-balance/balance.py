t = int(input())

for _ in range(t):
    n = int(input())

    ll = [2 ** i for i in range(1, n + 1)]
    ll = [ll[-1]] + ll[:-1]

    result = sum(ll[: n // 2]) - sum(ll[n // 2 :])
    print(result)
