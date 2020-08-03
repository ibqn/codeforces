_ = int(input())

reports_in_folder = [0]

reports = list(map(int, input().split()))


neg = 0
folder = 0
for r in reports:
    if r < 0:
        neg += 1

    if neg > 2:
        neg = 1
        folder += 1
        reports_in_folder.append(0)

    reports_in_folder[folder] += 1

print(folder + 1)
print(*reports_in_folder)

