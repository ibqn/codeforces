from functools import reduce

numbers = [int(input()) for _ in range(3)]

add = lambda num: sum(num)
mult = lambda num: reduce(lambda x, y: x*y, num)

def sum_mult_br(num):
    a, b, c = num
    return (a + b) * c

def sum_mult(num):
    a, b, c = num
    return a + b * c

def mult_sum(num):
    a, b, c = num
    return a * b + c

def mult_sum_br(num):
    a, b, c = num
    return a * (b + c)

operations = [add, mult, sum_mult, sum_mult_br, mult_sum, mult_sum_br]

result = 0
for op in operations:
    result = max(result, op(numbers))

print(result)
