from itertools import takewhile

n = int(input())

count = sum([1 for i in takewhile(lambda i: n // i > 1, range(1, n)) if n % i == 0 ])

print(count)