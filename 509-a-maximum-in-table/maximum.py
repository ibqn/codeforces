n = int(input())


def sum(i, j, memo={}):
    if i == 1 or j == 1:
        return 1

    if (min(i, j), max(i, j)) in memo:
        return memo[(min(i, j), max(i, j))]

    val = sum(i - 1, j, memo) + sum(i, j - 1, memo)
    memo[(min(i, j), max(i, j))] = val
    return val


print(sum(n, n))

