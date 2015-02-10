class AI(object):

    def move(board, letter):
        if letter == 'X':
            p_letter = 'O'
        else:
            p_letter = 'X'
        return win_move(board, letter) or block_move(board, p_letter) or move_corner(board) or move_center(board) or move_side(board)

## 1. Check if computer can make winning move
#def win_move(board, letter):
#    print "win move"
#    for number in range(0, 9):
#        try_board = board.get_copy_board()
#        print try_board.board
#        if try_board.is_empty(number):
#            try_board.board[number] = letter
#            print try_board.board
#            if try_board.win(letter):
#                return number
#    else: 
#        return False
#
## 2. Check if computer can block player from winning
#def block_move(board, letter):
#    print "block move"
#    for number in range(0, 9):
#        try_board = board.get_copy_board()
#        if try_board.is_empty(number):
#            try_board.board[number] = letter
#            if try_board.win(letter):
#                return number
#    else: 
#        return False
#
## 3. Take a corner piece (first one computer finds)
#def move_corner(board):
#    print "corner move"
#    for number in [0, 2, 6, 8]:
#        if board.is_empty(number):
#            return number
#    else: 
#        return False
#
## 4. Take center
#def move_center(board):
#    print "center move"
#    if board.is_empty(5):
#        return 5
#    else: 
#        return False
#
## 5. Take side (first one computer finds)
#def move_side(board):
#    print "side move"
#    for number in [1, 3, 5, 7]:
#        if board.is_empty(number):
#            return number
#    else: 
#        return False
#
