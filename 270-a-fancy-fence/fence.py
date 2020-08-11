t = int(input())

degrees = [int(input()) for _ in range(t)]

answers = ["YES" if 360 % (180 - a) == 0 else "NO" for a in degrees]

print(*answers, sep="\n")

