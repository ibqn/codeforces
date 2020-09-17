n, m = map(int, input().split())

snake = [
    "#" * m,
    "." * (m - 1) + "#",
    "#" * m,
    "#" + "." * (m - 1),
]

for i in range(n):
    print(snake[i % len(snake)])
