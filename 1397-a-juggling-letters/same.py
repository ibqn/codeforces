t = int(input())

for _ in range(t):
    n = int(input())

    letters = []
    for _ in range(n):
        letters += list(input())

    for l in set(letters):
        c = letters.count(l)
        if c % n != 0:  # or c // n < 1:
            print("NO")
            break
    else:
        print("YES")
