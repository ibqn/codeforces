t = int(input())

for _ in range(t):
    n = int(input())

    even = {False: 0, True: 0}

    nums = map(int, input().split())

    for i, v in enumerate(nums):
        even[i % 2 == 0] += int(i % 2 != v % 2)

    print(even[True] if even[True] == even[False] else -1)
