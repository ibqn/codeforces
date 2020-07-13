n, x, y = map(int, input().split())

s = n//2

print('NO' if x >= s and x <= s + 1 and y >= s and y <= s + 1 else 'YES')