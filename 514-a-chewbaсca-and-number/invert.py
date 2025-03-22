num = input()

res = ""
for n in num:
    i = int(n)
    res += str(9 - i) if i > 4 else n

if res[0] == "0":
    res = "9" + res[1:]

print(res)
