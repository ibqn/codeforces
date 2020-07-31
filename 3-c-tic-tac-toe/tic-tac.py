
fields = [c for _ in range(3) for c in input()]

# print(*fields)

diff = fields.count('X') - fields.count('0')

def check_win():
    counts = {}
    for p in "X0":
        for i in [0, 3, 6]:
            if fields[i:i + 3].count(p) == 3:
                counts[p] = counts.get(p, 0) + 1

        for i in [0, 1, 2]:
            if fields[i::3].count(p) == 3:
                counts[p] = counts.get(p, 0) + 1

        if fields[0::4].count(p) == 3 or fields[2:-1:2].count(p) == 3:
            counts[p] = counts.get(p, 0) + 1

    if len(counts.keys()) == 2:
        return 'illegal'

    for i, p in enumerate('0X'):
        if counts.get(p, 0) > 0:
            if i == diff:
                return p
            else:
                return 'illegal'

    return '.'


def evaluate():
    answer = 'illegal'

    if diff < 0 or diff > 1:
        return answer
    elif diff == 0:
        answer = 'first'
    elif diff == 1:
        answer = 'second'

    state = check_win()
    # print('state', state)

    if state == 'X':
        answer = 'the first player won'
    elif state == '0':
        answer = 'the second player won'
    elif state == 'illegal':
        return state
    elif fields.count('.') == 0:
        answer = 'draw'

    return answer


print(evaluate())
