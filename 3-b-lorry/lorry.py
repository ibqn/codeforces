n, capacity = map(int, input().split())

kayaks, catamarans = [], []

for i in range(n):
    vehicle_type, vehicle_capacity = map(int, input().split())
    l = kayaks if vehicle_type == 1 else catamarans
    l.append(( vehicle_capacity, i + 1 ))

kayaks.sort(key=lambda item: item[0], reverse=True)
catamarans.sort(key=lambda item: item[0], reverse=True)

# print('kayaks', kayaks, 'catamarans', catamarans)

max_capacity = 0
kayaks_cap = [0]
catamarans_cap = [0]

for i in range(min(capacity, len(kayaks))):
    kayaks_cap.append(kayaks_cap[i] + kayaks[i][0])

for i in range(min(capacity // 2, len(catamarans))):
    catamarans_cap.append(catamarans_cap[i] + catamarans[i][0])

# print('kayaks caps', kayaks_cap, 'catamarans caps', catamarans_cap)

kayaks_idx = 0
catamarans_idx = 0
for i, k in enumerate(kayaks_cap):
    if i > capacity:
        break

    idx = min((capacity - i) // 2, len(catamarans_cap) - 1)
    if (k + catamarans_cap[idx] > max_capacity):
        max_capacity = k + catamarans_cap[idx]
        kayaks_idx = i
        catamarans_idx = idx

print(max_capacity)

for i in range(kayaks_idx):
    print(kayaks[i][1], end=' ')

for i in range(catamarans_idx):
    print(catamarans[i][1], end=' ')


