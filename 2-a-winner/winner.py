n = int(input())

scores = {}
history = []

for i in range(n):
    name, points = input().split()

    scores[name] = scores.get(name, 0) + int(points)
    history.append((name, scores[name]))

max_score = max(scores.values())

gen = (
    name for (name, score) in history
    if scores[name] == max_score and score >= max_score
)
winner = next(gen)

print(winner)
