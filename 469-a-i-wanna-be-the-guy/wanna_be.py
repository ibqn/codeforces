n = int(input())

x = list(map(int, input().split()))[1:]
y = list(map(int, input().split()))[1:]

if set(range(1, n + 1)) == set(x + y):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
