n = int(input())

count = 0

i = 1
while n // i > 1:
    if n % i == 0:
        count += 1

    i += 1


print(count)