rides, count, single_ticket, group_ticket = map(int, input().split())

# single = [r * single_ticket for r in range(1 + rides)]
# group = [g * group_ticket for g in range(1 + (rides + count - 1) // count)]
# prices = [g + single_ticket * max(0, rides - count * i) for i, g in enumerate(group)]

prices = [
    group_ticket * i + single_ticket * max(0, rides - count * i)
    for i in range(1 + (rides + count - 1) // count)
]

# print(*prices)

print(min(prices))
