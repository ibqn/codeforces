n, c = map(int, input().split())

one, two = 1, 2


a, b = [], []

for i in range(n):
    veh_type, veh_cap = map(int, input().split())
    l = a if veh_type == 1 else b
    l.append(( veh_cap, i + 1 ))

a.sort(key=lambda t: t[0], reverse=True)
b.sort(key=lambda t: t[0], reverse=True)

print('ones', a, 'twos', b)


def idx(l, i):
    try:
        return l[i][0]
    except IndexError:
        return 0

l = []
m = n
while m > 0:
    if idx(a, 0) > idx(b, 0):
        l.append((one, *a.pop(0)))
        m-=1
    elif idx(a, 0) + idx(a, 1) > idx(b, 0):
        l.append((one, *a.pop(0)))
        l.append((one, *a.pop(0)))
        m-=2
    else:
        l.append((two, *b.pop(0)))
        m-=1

print(l)

tot_cap = 0
tot_typ = []
while c > 0 and n > 0:
    veh_type, cap, idx = l.pop(0)
    # print('type', veh_type, "cap", cap)

    if c >= veh_type:
        c -= veh_type
        tot_cap += cap
        tot_typ.append(idx)
    n -= 1

print(tot_cap)
print(" ".join(tot_typ))
