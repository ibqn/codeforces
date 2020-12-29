n = int(input())


def sum(i, j, memo={}):
    if i == 1 or j == 1:
        return 1

    key = (min(i, j), max(i, j))
    if key in memo:
        return memo[key]

    val = sum(i - 1, j, memo) + sum(i, j - 1, memo)
    memo[key] = val
    return val


print(sum(n, n))

