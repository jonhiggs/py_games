#!/usr/bin/env python
import random
from sys import exit

COMPUTER_GUESS = random.randint(1,20)
TRIES = 6
NAME = raw_input("What is your name? ")

def guess(number, attempt):
    if number < COMPUTER_GUESS:
        print("Too low!")

    if number > COMPUTER_GUESS:
        print("Too high!")

    if number == COMPUTER_GUESS:
        print("YESSSSS %s, you won, and it only took you %s guesses" %(NAME,attempt))
        exit()


print("Hello %s! Please guess the number between 1 and 20." %(NAME) )
print("You get %s tries" %(TRIES) )

for attempt in xrange(TRIES):
    guess(int(raw_input("take a guess: ")), attempt+1)

print("You lose, the number I was thinking of was %s" %(COMPUTER_GUESS) )
