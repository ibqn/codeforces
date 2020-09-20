t = int(input())


for _ in range(t):
    n = input()
    l = len(n) - 1

    nums = [d + "0" * (l - i) for i, d in enumerate(n) if d != "0"]
    print(len(nums))
    print(*nums)
