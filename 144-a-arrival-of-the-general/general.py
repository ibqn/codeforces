n = int(input())

row = list(map(int, input().split()))

min_i = 0
max_i = 0

for i in range(1, n):
    if row[i] <= row[min_i]:
        min_i = i

    if row[i] > row[max_i]:
        max_i = i

result = max_i + n - 1 - min_i - int(max_i > min_i)

print(result)

