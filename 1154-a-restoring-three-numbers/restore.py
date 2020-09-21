nums = sorted(map(int, input().split()))

abc = [nums[-1] - i for i in nums[:-1]]

print(*abc)
