t = int(input())

for _ in range(t):
    x, y, n = map(int, input().split())

    answer = x * (n // x) + y - (x if n % x < y else 0)

    print(answer)
