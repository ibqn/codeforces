
word = input()

counts = [ word.count(c) for c in set(word) ]

print(sum(map(lambda val: val ** 2, counts)))