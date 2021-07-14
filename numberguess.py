import random
secretNumber = random.randint(1, 20)

for guessesTaken in range(1,7):
   print('Take a guess:')
   guess = int(input())

   if guess < secretNumber:
       print('Your guess is smaller than secretNumber')
   elif guess > secretNumber:
        print('Your guess is greater than secretNumber')
   else:
        break

if guess == secretNumber:
    print('Good job you have found the secretNumber ' + str(secretNumber) + ' guesses')
else:
    print('No, the secretNumber which I guessed is ' + str(secretNumber) )



