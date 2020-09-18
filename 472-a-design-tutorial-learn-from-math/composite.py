n = int(input())


def composite(n):
    i = 2
    while i <= n / i:
        if n % i == 0:
            return True
        i += 1

    return False


i = 4
while i <= n - i:
    if composite(i) and composite(n - i):
        break
    i += 1

print(i, n - i)
