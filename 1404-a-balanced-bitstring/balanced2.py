t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    bitstring = input()
    zero = 0
    one = 0
    answer = True
    for j in range(k):
        balanced = "?"
        for i in range(j, n, k):
            if bitstring[i] != "?":
                if balanced != "?":
                    if balanced != bitstring[i]:
                        answer = False
                        break
                else:
                    balanced = bitstring[i]
        if not answer:
            break

        if balanced == "1":
            one += 1
        elif balanced == "0":
            zero += 1

    if answer:
        answer = max(one, zero) <= k // 2

    print("YES" if answer else "NO")

