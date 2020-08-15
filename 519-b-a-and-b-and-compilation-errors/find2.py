n = int(input())

orig = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

orig.sort()
second.sort()
third.sort()


def find_missing(orig, ref):
    gen = (orig[i] for i, v in enumerate(ref) if orig[i] != v)
    return next(gen, orig[-1])


print(find_missing(orig, second))
print(find_missing(second, third))

