n = int(input())

line = "".join(input().split())

scores = []

for i in range(n):
    ones_before = line[:i].count("1")
    for j in range(i, n):
        zeros = line[i : j + 1].count("0")
        ones_after = line[j + 1 :].count("1")
        scores.append(ones_before + zeros + ones_after)

print(max(scores))
