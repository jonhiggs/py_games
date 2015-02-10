# Inspired by "Invent Your Own Computer Games with Python
# 2nd Edition" by Al Sweigart

from time import sleep
import copy

from ai import *
from player import *
from board import *

# class Game():
#   pass 

play_again = True
computer_thinking = 0.1


def print_example_board():
    print "To play, please enter the number of the field."
    print "See the illustration below"
    print '''
   |   |
 1 | 2 | 3
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 7 | 8 | 9
   |   |
'''

# Main part of game
while play_again:
    # Do the setup - part of every new game
    print "\nWelcome to Tic Tac Toe! \n"
    board = Board()

    while True:
        board.player_token = raw_input('Do you want to play "X" or "O"?: ')
        if board.player_token: break

    #player = Player()
    #ai = AI

    print "Player is %s, computer is %s" % (board.player_token, board.ai_token)
    print ("\n")
    print_example_board()
    print ("\n")
    print "Computer will randomly decided who will make the first move..."
    sleep(computer_thinking)

    if board.player_turn:
        turn = "Player"
    else:
        turn = "AI"
    print "%s will make the first move" % turn

    sleep(computer_thinking)
    #Draw board & get computer and player feedback until
    #one player wins or there is a tie

    #while True:
    #    # check for tie - board is full and no one won
    #    if new_board.is_full():
    #        print "It's a tie!"
    #        break
    #    else:
    #        if turn == 'Player':
    #            print "Players turn: ",
    #            move = player_move(new_board)
    #            new_board.make_move(move, player_letter)
    #            new_board.print_board()
    #            if new_board.win(player_letter):
    #                print "Player wins!"
    #                break
    #            else:
    #                turn = 'Computer'
    #        else:
    #            print "Computers turn..."
    #            sleep(computer_thinking)
    #            move = computer_move(new_board, computer_letter)
    #            new_board.make_move(move, computer_letter)
    #            new_board.print_board()
    #            if new_board.win(computer_letter):
    #                print "Computer wins!"
    #                break
    #            else:
    #                turn = 'Player'#

    #play_again = raw_input("Do you want to play again?"
    #                       "(Y)es/(N)o: ").lower().startswith('y')
