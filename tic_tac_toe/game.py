from random import randint

from ai import *
from human import *

class Game(object):

    def __init__(self):
        players = 2
        self._next_player = randint(0,(players-1))

        self._moves = []
        for player in range(0,players):
            human = raw_input('Are you human? (y/n): ')
            if human in ['y']:
                self._players[player] = Player()
            else:
                self._players[player] = AI()

        self._board = Board()



    @property
    def next_player(self):
        if self._next_player == self._players:
            self._next_player = 0
        else:
            self._next_player += 1

        return self._next_player
