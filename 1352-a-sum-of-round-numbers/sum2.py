t = int(input())

for _ in range(t):
    n = int(input())

    factor = 1
    while factor <= n // 10:
        factor *= 10

    nums = []
    while factor > 0:
        v = n // factor
        if v:
            nums.append(v * factor)
        n = n % factor

        factor //= 10

    print(len(nums))
    print(*nums)
