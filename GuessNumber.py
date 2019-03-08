def guessNumber(a):
    if a < guessAnswer:
        print('Your guess is too low.')
        return True
    elif a > guessAnswer:
        print('Your guess is too high.')
        return True
    elif a == guessAnswer:
        return False

import random
print('I am thinking of a number between 1 and 20.')
guessAnswer = random.randint(1,20)
i = 1
guess = int(input('Take a guess: '))
while guessNumber(guess):
    guess = int(input('Take a guess: '))
    i += 1
print('Good job! You guessed my number in ', i, ' guesses!')
