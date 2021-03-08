import random

number = random.randint(1, 51)

print('I am thinking of a number between 1 and 50.')

guess = 0
count = 0

while guess != number:
    print('Take a guess.')
    guess = int(input())

    count += 1

    if guess > number:
        print('Your guess is too high.')

    else:
        print('Your number is too low.')

print(f'Good job! You guessed my number in {count} guesses.')