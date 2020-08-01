a, b, c = [int(input()) for _ in range(3)]

operations = [
    a + b + c,
    a * b * c,
    (a + b) * c,
    a * b + c,
    a * (b + c),
]

print(max(operations))
