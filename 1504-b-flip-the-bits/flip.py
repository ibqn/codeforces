n = int(input())

for _ in range(n):
    l = int(input())
    a, b = input() + "0", input() + "0"

    count = 0
    for i in range(l):
        count += (a[i] == "1") - (a[i] == "0")

        if (a[i] == b[i]) != (a[i + 1] == b[i + 1]) and count != 0:
            print("NO")
            break
    else:
        print("YES")
