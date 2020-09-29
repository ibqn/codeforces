n = int(input())

counts = 0
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        counts += 1 if int(a > b) else -1

if counts == 0:
    result = "Friendship is magic!^^"
elif counts > 0:
    result = "Mishka"
else:
    result = "Chris"

print(result)
