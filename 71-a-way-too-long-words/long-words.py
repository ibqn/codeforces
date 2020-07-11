w = int(input())

words = []


def abbreviate_word(word):
    word_length = len(word)

    if  word_length <= 10:
        return word

    return word[0] + str(word_length - 2) + word[-1]


for _ in range(w):
    words.append(abbreviate_word(input()))

for word in words:
    print(word)

    