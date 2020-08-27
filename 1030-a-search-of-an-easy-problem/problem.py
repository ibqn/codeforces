_ = int(input())

responses = map(bool, map(int, input().split()))

answer = "hard" if any(responses) else "easy"

print(answer)
