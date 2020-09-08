t = int(input())

for _ in range(t):
    n = int(input())

    array = list(map(int, input().split()))

    answer = 0

    for a in array:
        answer = max(0, answer + a)

    print(answer)

