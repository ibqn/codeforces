n, _ = list(map(int, input().split()))

gen = (c for _ in range(n) for c in input() if c in "CMY")

if not list(gen):
    print("#Black&White")
else:
    print("#Color")
