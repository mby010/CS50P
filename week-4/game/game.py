from random import randint
import sys

while True:
    try:
        n = int(input('Level: '))
        if n < 1:
            raise ValueError
        x = randint(1, n)
        guess = int(input('Guess: '))
        if guess > x:
            print('Too large!')
        elif guess < x:
            print('Too small!')
        else:
            sys.exit('Just right!')

    except ValueError:
        pass
