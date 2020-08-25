yaer = int(input())

answer = yaer + 1
while not len(set(str(answer))) == 4:
    answer += 1

print(answer)
