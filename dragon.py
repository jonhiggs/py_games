#!/usr/bin/env python
from random import randint
from time import sleep

def displayIntro():
    print('''\nYou are in a land filled with MONSTERS. In front of you you see
            two caves. One cave houses a FRIENDLY monster, that will share cake 
            and balloons with you. The OTHER cave though... houses an EVIL
            monster that will eat you on sight.\n''')

def chooseCave():
    cave = 0   # TODO: work out how to make this not needed. There will be a way.
    while cave != 1 and cave != 2:
        cave = int(raw_input("Do you choose cave 1 or 2? "))

    return checkCave(cave)

def checkCave(chosenCave):
    print('You approach the cave...')
    sleep(3)
    print('It is dark and spooky...')
    sleep(3)
    print('A large monster out in front of you! He opens his jaws and... \n')
    sleep(2)

    friendlyCave = randint(1,2)

    if chosenCave == friendlyCave:
        print("Showers you with champagne! Good choice young one!\n")
    else:
        print("EATS YOU UP AND SPITS YOU OUT!\n")

play_again = True

while play_again:
   displayIntro()
   chooseCave()
   play = raw_input("Do you want to play again? (y)es or (n)o: ")
   play_again = (play == "yes" or play == "y")
