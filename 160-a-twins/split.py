n = int(input())

coins = list(map(int, input().split()))

coins.sort(reverse=True)

# print(coins)

def split(a, b):

    middle = a + (b - a) // 2

    # print("a", a, "b", b, "m", middle)
    
    if (a == b):
        # print("a", a, "b", b, "m", middle)
        return a


    if sum(coins[:middle + 1]) > sum(coins[middle + 1:]):
        return split(a, middle)
    else:
        return split(middle + 1, b)


idx = split(0, len(coins) - 1)

# print("index=", idx)

print(len(coins[:idx + 1]))

