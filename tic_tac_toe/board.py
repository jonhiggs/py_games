from game import *

class Board(Game):
    @property
    def position_available(self, position):
        positions = Game.players[0] | Game.players[1]
        if (self._postions & (1 << position) ) != 0:
            return False
        else:
            return True



    def print_board(self):
        # Make this function shorter
        print  '''
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
''' % (self.board[0], self.board[1], self.board[2], self.board[3], self.board[4],
       self.board[5], self.board[6], self.board[7], self.board[8])

    def make_move(self, move, letter):
         self.board[move] = letter
         return self.board


    def is_empty(self, index):
        return self.board[index] == ' '


    def is_full(self):
        #make this function shorter
        return ' ' not in self.board
            
    # this function will be redundant - we can make a new board object to try move
    def get_copy_board(self):
        return copy.deepcopy(self)

    def row(self, n):
        offset = (n*3)
        r = []
        for position in range(0,3):
            r.append(self.board[offset+position])
        return r

    def matrix(self):
        m = []
        for r in range(0,3):
            m.append(self.row(r))
        return m

    def win(self, player):
        return ((self.board[0] == self.board[1] == self.board[2] == player) or
                (self.board[3] == self.board[4] == self.board[5] == player) or
                (self.board[6] == self.board[7] == self.board[8] == player) or
                (self.board[0] == self.board[3] == self.board[6] == player) or
                (self.board[1] == self.board[4] == self.board[7] == player) or
                (self.board[2] == self.board[5] == self.board[8] == player) or
                (self.board[0] == self.board[4] == self.board[8] == player) or
                (self.board[2] == self.board[4] == self.board[6] == player))

    # put indexes in vars? row var/columnvar/diag var. Add corner var and side var
#    def row_win(self, player):
#        return ((self.board[0] == self.board[1] == self.board[2] == player) or
#                (self.board[3] == self.board[4] == self.board[5] == player) or
#                (self.board[6] == self.board[7] == self.board[8] == player))
#
#
#    def column_win(self, player):
#        return ((self.board[0] == self.board[3] == self.board[6] == player) or
#                (self.board[1] == self.board[4] == self.board[7] == player) or
#                (self.board[2] == self.board[5] == self.board[8] == player))
#
#
#    def diagonal_win(self, player):
#        return ((self.board[0] == self.board[4] == self.board[8] == player) or
#                (self.board[2] == self.board[4] == self.board[6] == player))
