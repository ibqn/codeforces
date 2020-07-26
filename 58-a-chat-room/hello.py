word = input()

def is_hello(word):
    idx = 0
    for c in 'hello':
        try:
            idx = word.index(c, idx) + 1
        except ValueError:
            return 'NO'

    return 'YES'

answer = is_hello(word)
print(answer)
