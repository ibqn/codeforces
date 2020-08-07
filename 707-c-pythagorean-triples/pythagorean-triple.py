n = int(input())

if n <= 2:
    print(-1)
else:
    if n % 2 == 0:
        a = n ** 2 // 4 - 1
        b = n ** 2 // 4 + 1
    else:
        a = (n ** 2 - 1) // 2
        b = (n ** 2 + 1) // 2

    print(a, b)
