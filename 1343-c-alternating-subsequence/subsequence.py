t = int(input())


for i in range(t):
    n = int(input())

    sequence = list(map(int, input().split()))

    sum_value = 0

    val = sequence[0]
    pos = sequence[0] > 0

    for v in range(1, n):
        if pos == (sequence[v] > 0):
            val = max(val, sequence[v])
        else:
            sum_value += val
            val = sequence[v]

        pos = sequence[v] > 0

    sum_value += val

    print(sum_value)
