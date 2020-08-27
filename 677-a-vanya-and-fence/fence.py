_, height = map(int, input().split())

heights = list(map(int, input().split()))

width = sum(2 if h > height else 1 for h in heights)

print(width)
