a, b = input(), input()

result = [str(int(f != s)) for (f, s) in zip(a, b)]

print("".join(result))
