class Player(object):

    def player_move(board):
        while True:
            move = raw_input("What move do you want to make? ")
            if move.isdigit():
                move = int(move)
                if move > 0 and move < 10 and board.is_empty(move-1):
                    return int(move) - 1
                elif move < 0 or move >= 10:
                    print "That number is off the charts! Try again!"
                else:
                    print "That position is already taken! Try again!"
            else:
                print "Please enter a NUMBER!"

    # def play_again():
