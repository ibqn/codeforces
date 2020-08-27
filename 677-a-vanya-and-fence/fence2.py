n, height = map(int, input().split())

heights = list(map(int, input().split()))

width = n + sum(1 for h in heights if h > height)

print(width)
