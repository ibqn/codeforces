import math

a, b = map(int, input().split())

# print(math.ceil(0.00001 + math.log(b / a) / math.log(3.0 / 2.0)))
print(int(math.log(b / a, 1.5)) + 1)