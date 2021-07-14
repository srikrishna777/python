import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guessTaken in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is smaller than secretNumber')
    elif guess > secretNumber:
        print('your guess is bigger than secretNumber')
    else:
        break

if guess == secretNumber:
    print('Good job! you guessed my number in' + str(guessTaken) + 'guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

