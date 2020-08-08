# we do not need this n anywhere
_ = int(input())

pillars = list(map(int, input().split()))

max_radius = max(pillars)

idx = pillars.index(max_radius)


def is_movable():
    for i in range(min(idx, len(pillars) - 1)):
        if not (pillars[i] < pillars[i + 1]):
            return "no"

    for i in range(idx, len(pillars) - 1):
        if not (pillars[i] > pillars[i + 1]):
            return "no"

    return "yes"


print(is_movable())

