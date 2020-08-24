n = int(input())

winners = input()

anton_wins = winners.count("A")

if anton_wins > n - anton_wins:
    print("Anton")
elif anton_wins < n - anton_wins:
    print("Danik")
else:
    print("Friendship")
