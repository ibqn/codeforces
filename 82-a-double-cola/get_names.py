n = int(input())

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

i = 1
q = 5

while n > q:
    n -= q
    i += 1
    q *= 2
    # print("i", i, "n", n, "q", q)

l = 2 ** (i - 1)
ii = (n + l - 1) // l - 1
# print("i", i, "n", n, "ii", ii)

print(names[ii])
