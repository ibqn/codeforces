t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    bitstring = input()
    balanced = ["?"] * k

    answer = True
    for j in range(k):
        for i in range(j, n, k):
            if bitstring[i] != "?":
                if balanced[j] != "?":
                    if balanced[j] != bitstring[i]:
                        answer = False
                        break
                else:
                    balanced[j] = bitstring[i]
        if not answer:
            break

    if answer:
        q = balanced.count("?")
        # z = balanced.count("0")
        o = balanced.count("1")
        r = k // 2 - o
        answer = r >= 0 and q >= r

    print("YES" if answer else "NO")

