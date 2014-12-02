#!/usr/bin/env python
import random

COMPUTER_GUESS = random.randint(1,20)
guess_total = 0
tries = 6

name = raw_input("What is your name? ")

print("Hello %s! Please guess the number between 1 and 20." %(name) )
print("You get %s tries" %(tries) )

while guess_total < tries :
    guess = int(raw_input("take a guess: " ))
    guess_total += 1

    if guess < COMPUTER_GUESS:
        print("Too low!")
    elif guess > COMPUTER_GUESS:
        print("Too high!")
    elif guess == COMPUTER_GUESS:
        break
    else:
        print("oops, something went wrong")

if guess == COMPUTER_GUESS:
    print("YESSSSS %s, you won, and it only took you %s guesses" %(name,guess_total))
else:
    print("You lose, the number I was thinking of was %s" %(COMPUTER_GUESS) )
