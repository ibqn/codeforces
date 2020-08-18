n, k = map(int, input().split())

powers = list(map(int, input().split()))

max_power = max(powers)


def get_winner():
    i = 0
    while True:
        if powers[i] == max_power:
            return powers[i]

        for j in range(i + 1, min(i + k + int(i == 0), n)):
            if powers[i] < powers[j]:
                i = j
                break
        else:
            return powers[i]


print(get_winner())
