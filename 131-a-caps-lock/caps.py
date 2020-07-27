word = input()

if word[1:].isupper():
    if word[0].isupper():
        print(word.lower())
    else:
        print(word[0].upper() + word[1:].lower())
elif len(word) == 1:
    print(word.upper() if word.islower() else word.lower())
else:
    print(word)
