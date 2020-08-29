n, c = map(int, input().split())

one, two = 1, 2


a, b = [], []

for i in range(n):
    veh_type, veh_cap = map(int, input().split())
    l = a if veh_type == 1 else b
    l.append(( veh_cap, i + 1 ))

a.sort(key=lambda el: el[0], reverse=True)
b.sort(key=lambda el: el[0], reverse=True)

# print('ones', a, 'twos', b)

tot_cap = 0
ai, bi = 0, 0
# al, bl = len(a), len(b)
tot_idx = []

def arr(l, i):
    return l[i][0] if i < len(l) else 0


while c > 0 and n > 0:
    if (c == 1 and ai < len(a)) or arr(a, ai) > arr(b, bi):
        cap, idx = a[ai]
        tot_cap += cap
        tot_idx.append(idx)
        ai += 1
        c -= 1
        n -= 1
    elif arr(a, ai) + arr(a, ai + 1) > arr(b, bi):
        cap1, idx1 = a[ai]
        cap2, idx2 = a[ai + 1]
        tot_cap += cap1 + cap2
        tot_idx.append(idx1)
        tot_idx.append(idx2)
        ai += 2
        c -= 2
        n -= 2
    else:
        cap, idx = b[bi]
        tot_cap += cap
        tot_idx.append(idx)
        bi += 1
        c -= 2
        n -= 2

print(tot_cap)
print(" ".join(map(str, tot_idx)))


