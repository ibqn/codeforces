n = int(input())

result = 0
for i in range(n):
    statement = input()
    if '+' in statement:
        result += 1
    else:
        result -= 1

print(result)