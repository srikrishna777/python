import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessTaken in range(1,8):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is smaller than secretNumber')
    elif guess > secretNumber:
        print('Your guess is bigger than secretNumber')
    else:
        break

if guess == secretNumber:
    print('Good job you have found the secretNumber ' + str(secretNumber) + ' guesses')
else:
    print('Nope. The number I was thinking of was' + str(secretNumber))




