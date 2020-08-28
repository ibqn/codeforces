n = int(input())

layers = ["hate", "love"]

feeling = ""
for i in range(n):
    feeling += f"I {layers[i % 2]} {'it' if i == n - 1 else 'that '}"

print(feeling)
