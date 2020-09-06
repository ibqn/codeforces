t = int(input())

for _ in range(t):
    n = int(input())

    split = False
    a = ""
    b = ""
    for c in input():
        if split:
            a += "0"
            b += c
        elif c == "2":
            a += "1"
            b += "1"
        elif c == "0":
            a += "0"
            b += "0"
        else:
            split = True
            a += "1"
            b += "0"

    print(a)
    print(b)

