t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    answer = (abs(a - b) + 9) // 10
    print(answer)
