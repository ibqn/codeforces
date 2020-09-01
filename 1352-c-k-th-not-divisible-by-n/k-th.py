t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    print(k // (n - 1) * n + (k % (n - 1) if k % (n - 1) != 0 else -1))
