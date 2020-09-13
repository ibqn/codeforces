guest_name = input()
host_name = input()
pile = input()

result = sorted(guest_name + host_name) == sorted(pile)

print("YES" if result else "NO")
