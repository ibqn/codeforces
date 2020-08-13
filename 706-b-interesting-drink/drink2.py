import bisect

_ = int(input())

prices = list(map(int, input().split()))

prices.sort()

# print(*prices)

days_num = int(input())


for _ in range(days_num):
    q = int(input())

    print(bisect.bisect_right(prices, q))
