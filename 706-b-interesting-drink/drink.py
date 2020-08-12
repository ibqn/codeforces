_ = int(input())

prices = list(map(int, input().split()))

prices.sort()

days_num = int(input())

# find smallest prices
def find_smallest(budget, prices, left=0, right=len(prices)):

    if left >= right:
        return left

    middle = (right + left) // 2

    # print(left, middle, right, prices[middle] > budget)

    if prices[middle] > budget:
        return find_smallest(budget, prices, left, middle)
    else:
        return find_smallest(budget, prices, middle + 1, right)


for _ in range(days_num):
    q = int(input())

    print(find_smallest(q, prices))


# print(*prices)
