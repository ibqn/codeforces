n = int(input())


def is_beaufiful(num):
    vals = {v: num.count(v) == 1 for v in str(num)}
    return all(vals)


answer = n + 1
while not is_beaufiful(answer):
    answer += 1

print(answer)
