t = int(input())

for _ in range(t):
    n = int(input())

    k = 1
    more = True

    while more:
        k += 1
        candies = 2 ** k - 1
        more = n % candies != 0

    print(n // candies)
