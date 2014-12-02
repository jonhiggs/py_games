#!/usr/bin/env python
import random
from sys import exit

COMPUTER_GUESS = random.randint(1,20)
guess_total = 0
tries = 6

# TODO: name should be constant.
name = raw_input("What is your name? ")

print("Hello %s! Please guess the number between 1 and 20." %(name) )
print("You get %s tries" %(tries) )

def guess(number, attempt):
    if number < COMPUTER_GUESS:
        print("Too low!")

    if number > COMPUTER_GUESS:
        print("Too high!")

    if number == COMPUTER_GUESS:
        print("YESSSSS %s, you won, and it only took you %s guesses" %(name,attempt))
        exit()

for attempt in xrange(tries):
    guess(int(raw_input("take a guess: ")), attempt+1)

print("You lose, the number I was thinking of was %s" %(COMPUTER_GUESS) )
