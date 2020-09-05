calories = list(map(int, input().split()))
answer = sum(calories[int(i) - 1] for i in input())

print(answer)
