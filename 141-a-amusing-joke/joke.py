from collections import Counter

guest = input()
residence = input()
pile = input()

c1 = Counter(guest + residence)
c2 = Counter(pile)
result = c1 == c2

print("YES" if result else "NO")

