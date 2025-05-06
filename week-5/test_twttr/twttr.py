def main():
    phrase = input('Input: ')
    print(shorten(phrase))

print(f'Output: {phrase}')

def shorten(phrase):
    for c in phrase:
        if c in ['a', 'A', 'E', 'e', 'I', 'i', 'U', 'u', 'O', 'o']:
        phrase = phrase.replace(c, '')
    return phrase

if __name__ == "__main__":
    main()

