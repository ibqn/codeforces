t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    rest = a % b
    moves = b - rest if rest else 0
    print(moves)
