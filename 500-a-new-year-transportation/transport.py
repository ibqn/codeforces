_, t = map(int, input().split())

board = list(map(int, input().split()))

i = 1
while i < t:
    i += board[i - 1]

if i == t:
    print("YES")
else:
    print("NO")
