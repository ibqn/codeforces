n = int(input())

inl = list(map(int, input().split()))

outl = [ inl.index(i + 1) + 1 for i in range(n) ]

print(*outl)
