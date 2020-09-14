t = int(input())

for _ in range(t):
    n = int(input())
    answer = (n - int(n % 2 == 0)) // 2
    print(answer)

