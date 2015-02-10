class Human(Game):

    def __init__(self):
        # create a list like this ' ' * 9
        self._token = None
        self._moves = '0b000000000'

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        # token could be anything
        value = value.upper()
        if value == "X" or value == "O":
            self._player1_token = value

