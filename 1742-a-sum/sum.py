n = int(input())

for _ in range(n):
    numbers = list(map(int, input().split()))
    answer = "yes" if sum(numbers) == 2 * max(numbers) else "no"
    print(answer)
