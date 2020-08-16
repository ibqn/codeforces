_, m = map(int, input().split())

prices = list(map(int, input().split()))

fruits = {}

for _ in range(m):
    name = input()
    fruits[name] = fruits.get(name, 0) + 1

sorted_fruits = sorted(fruits.values(), reverse=True)
sorted_prices = sorted(prices)
reverced_prices = sorted_prices[::-1]

# print(*sorted_fruits)
# print(*sorted_prices)

min_price = sum([v * sorted_prices[i] for i, v in enumerate(sorted_fruits)])
max_price = sum([v * reverced_prices[i] for i, v in enumerate(sorted_fruits)])

print(min_price, max_price)
