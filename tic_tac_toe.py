# Inspired by "Invent Your Own Computer Games with Python,
# 2nd Edition" by Al Sweigart

from random import randint
from time import sleep

play_again = True
computer_thinking = 2


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


def print_board(board):
    print '''
   |   |
 %s | %s | %s
   |   |
-----------
   |   |
 %s | %s | %s
   |   |
-----------
   |   |
 %s | %s | %s
   |   |
''' % (board[0], board[1], board[2], board[3], board[4],
       board[5], board[6], board[7], board[8])


def first_move():
    if randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'


def get_player_letter():
    while True:
        player_letter = raw_input("Do you want to play"
                                  " \"X\" or \"O\"? :").upper()
        if player_letter != 'X' and player_letter != 'O':
            print "Does not compute, please choose again"
        else:
            if player_letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']


def make_move(board, move, letter):
    board[move] = letter
    return board


def is_empty(board, index):
    return board[index] == ' '


def is_full(board):
    if ' ' not in board:
        return True
    else:
        return False


def player_move(board):
    while True:
        move = raw_input("What move do you want to make? ")
        if move.isdigit():
                move = int(move)
                if move > 0 and move < 10 and is_empty(board, move-1):
                    return int(move) - 1
                elif move < 0 or move >= 10:
                    print "That number is off the charts! Try again!"
                else:
                    print "That position is already taken! Try again!"
        else:
            print "Please enter a NUMBER!"


def computer_move(board, letter):
    if letter == 'X':
        p_letter = 'O'
    else:
        p_letter = 'X'
    return win_move(board, letter) or block_move(board, p_letter) or move_corner(board) or move_center(board) or move_side(board)

# 1. Check if computer can make winning move
def win_move(board, letter):
    for number in range(0, 9):
        try_board = get_copy_board(board)
        if is_empty(try_board, number):
            try_board[number] = letter
            if win(try_board, letter):
                return number
    else: 
        return False

# 2. Check if computer can block player from winning
def block_move(board, letter):
    for number in range(0, 9):
        try_board = get_copy_board(board)
        if is_empty(try_board, number):
            try_board[number] = letter
            if win(try_board, letter):
                return number
    else: 
        return False

# 3. Take a corner piece (first one computer finds)
def move_corner(board):
    for number in [0, 2, 6, 8]:
        print number
        print is_empty(board,number)
        if is_empty(board, number):
            return number
    else: 
        return False

# 4. Take center
def move_center(board):
    if is_empty(board, 5):
        return 5
    else: 
        return False

# 5. Take side (first one computer finds)
def move_side(board):
    for number in [1, 3, 5, 7]:
        if is_empty(board, number):
            return number
    else: 
        return False


def get_copy_board(board):
    return list(board)


def win(board, player):
    return (row_win(board, player) or column_win(board, player) or
            diagonal_win(board, player))


def row_win(board, player):
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player))


def column_win(board, player):
    return ((board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player))


def diagonal_win(board, player):
    return ((board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))

# Main part of game
while play_again:
    # Do the setup - part of every new game
    board = [' '] * 9
    print "\nWelcome to Tic Tac Toe! \n"
    player_letter, computer_letter = get_player_letter()
    print "Player is %s, computer is %s" % (player_letter, computer_letter)
    print ("\n")
    print_example_board()
    print ("\n")
    print "Computer will randomly decided who will make the first move..."
    sleep(computer_thinking)
    turn = first_move()
    print "%s will make the first move" % turn
    sleep(computer_thinking)
# Draw board & get computer and player feedback until
# one player wins or there is a tie
    while True:
        # check for tie - board is full and no one won
        if is_full(board):
            print "It's a tie!"
            break
        else:
            if turn == 'Player':
                print "Players turn: ",
                move = player_move(board)
                make_move(board, move, player_letter)
                print_board(board)
                if win(board, player_letter):
                    print "Player wins!"
                    break
                else:
                    turn = 'Computer'
            else:
                print "Computers turn..."
                sleep(computer_thinking)
                move = computer_move(board, computer_letter)
                make_move(board, move, computer_letter)
                print_board(board)
                if win(board, computer_letter):
                    print "Computer wins!"
                    break
                else:
                    turn = 'Player'

    play_again = raw_input("Do you want to play again?"
                           "(Y)es/(N)o: ").lower().startswith('y')
