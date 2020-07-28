n = int(input())

digits = '47'

l1 = [c for c in digits]

perm = lambda arr1, arr2: [a1 + a2 for a1 in arr1 for a2 in arr2]

arr = ['']
res = []
for i in range(4):
    arr = perm(arr, l1)
    res += arr

# print(res)

def is_lucky(n):
    for r in res:
        if n % int(r) == 0:
            return'YES'

    return 'NO'

print(is_lucky(n))



