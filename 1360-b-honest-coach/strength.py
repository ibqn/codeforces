t = int(input())

for _ in range(t):
    n = int(input())
    strength = sorted(map(int, input().split()))
    difference = min(strength[i] - strength[i - 1] for i in range(1, len(strength)))
    print(difference)
