
class CleanBoard:
    """
    This consists of different possibilites
    a player can hit during the gameplay
    """

    def __init__(self):
        self.black = 9
        self.red = 1

    def strike(self):
        """
        When a player pockets a coin he/she wins a point
        The black coin gets reduced by 1

        """
        if self.black == 0:
            return 0

        self.black = self.black - 1
        return 1

    def multiStrike(self):
        """
        When a player pockets more than one coin he/she wins 2 points. All, but 2
        coins, that were pocketed, get back on to the carrom-board
        The black coin and red coin is reset to 7 and 1 respectively.

        """
        if self.black == 0:
            return 0

        self.black = 7
        self.red = 1
        return 2

    def redStrike(self):
        """
        When a player pockets red coin he/she wins 3 points
        The Red Coin gets reduced by 1

        """
        if self.red == 0:
            return 0

        self.red = self.red - 1
        return 3

    def striker(self):
        """
        When a player pockets the striker he/she loses a point

        """
        return -1

    def defunt(self):
        """
        When a coin is thrown out of the board, due to a strike, the player
        loses 2 points, and the coin goes out of play
        And the Black Coin gets reduced by 1

        """
        if self.black == 0:
            return 0

        self.black = self.black - 1
        return -2

    def emptyStrike(self):
        """
        No coin is put inside the pocket.

        """
        return 0

    def coinCheck(self):
        """
        checks if the coins are pocketed or not.

        """
        if self.black == 0 and self.red == 0:
            return True
        else:
            return False