phrase = input('Input: ')
for c in phrase:
    if c in ['a', 'A', 'E', 'e', 'I', 'i', 'U', 'u', 'O', 'o']:
        phrase = phrase.replace(c, '')
print(f'Output: {phrase}')
