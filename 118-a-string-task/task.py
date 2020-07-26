str = input()

vowels = 'aoyeui'

for c in str:
    lc = c.lower()
    if lc not in vowels:
        print(f'.{lc}', end='')

print('')
