n = int(input())

inl = list(map(int, input().split()))

outl = [None] * n
for i in range(n):
    outl[inl[i] - 1] = i + 1

print(' '.join(map(str, outl)))
