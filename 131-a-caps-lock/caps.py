word = input()

print(word.swapcase() if word[1:] == word[1:].upper() else word)
