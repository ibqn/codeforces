n, a, b = map(int, input().split())

if 6 * n <= a * b:
    print(a * b)
    print(a, b)
else:
    swap = False
    if a > b:
        swap = True
        a, b = b, a

    i = a
    newa = a
    newb = (6 * n + a - 1) // a
    square = newa * newb

    while i * i <= 6 * n:
        tmpb = (6 * n + i - 1) // i

        if not tmpb < b and tmpb * i <= square:
            newa, newb, square = i, tmpb, tmpb * i

        i += 1

    if swap:
        newa, newb = newb, newa

    print(square)
    print(newa, newb)

