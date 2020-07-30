n, m = list(map(int, input().split()))

def is_color():
    for _ in range(n):
        row = input().split()
        gen = (c for c in row if c in 'CMY')
        for _ in gen:
            return True
    return False

print( "#Color" if is_color() else "#Black&White")

