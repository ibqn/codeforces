n, k = map(int, input().split())

participations = map(int, input().split())

answer = sum(1 for p in participations if 5 - p >= k) // 3

print(answer)
