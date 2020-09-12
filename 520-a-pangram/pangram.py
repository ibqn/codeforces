n = int(input())

letter_count = len(set(input().lower()))

print("YES" if letter_count == 26 else "NO")
