n = int(input())

orig = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

orig.sort()
second.sort()
third.sort()


def find_missing(orig, ref):
    for i, v in enumerate(ref):
        if orig[i] != v:
            return orig[i]

    return orig[-1]


# print("orig", *orig)
# print("second", *second)
# print("third", *third)

print(find_missing(orig, second))
print(find_missing(second, third))

