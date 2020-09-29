#guess the number 0-20

import random

number = random.randint(0, 20)
guess = int(input("Guess the number from 0 to 20: \n"))

while guess < 0 or guess > 20:
    print("Guess from 0 to 20!")
    guess = int(input("Guess the number from 0 to 20: \n"))

if guess == number:
    print("You guessed it right!")
else:
    print("You guessed wrong! The number was :\n" + str(number))
    