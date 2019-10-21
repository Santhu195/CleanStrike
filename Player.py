
import histories

class Players:
    """
    The Players class will consists of players score and their history of moves made during the game.
    """

    def __init__(self, player1score=0, player2score=0, player1history=[], player2history=[]):
        self.player1score = player1score
        self.player2score = player2score
        self.player1history = player1history
        self.player2history = player2history

    def checkplayerscore(self):
        """
        The following checks if a player score has exceeded by 5 points
    
        """
        if self.player1score >= 5 or self.player2score >= 5:
            return True

        return False

    def updateplayerscore(self, player, score):
        """
        The following updates a player score based on the player

        """
        if player == 1:
            self.player1score +=  score
            if self.player1score < 0:
                self.player1score = 0
        else:
            self.player2score +=  score
            if self.player2score < 0:
                self.player2score = 0

    def updateplayerhistory(self, player, outcome):
        """
        The following updates a player history based on the player

        """
        if player == 1:
            self.player1history.append({"outcome": outcome,
                                        "score": self.player1score})
        else:
            self.player2history.append({"outcome": outcome,
                                        "score": self.player2score})

    def getresult(self):
        """
        The following checks the score of a player and decalares the result.

        """
        if self.player1score > self.player2score and self.player1score - self.player2score >= 3:
            return {"result": "Player1",
                    "player1score": self.player1score,
                    "player2score": self.player2score}

        elif self.player1score < self.player2score and self.player2score - self.player1score >= 3:
            return {"result": "Player2",
                    "player1score": self.player1score,
                    "player2score": self.player2score}

        return {"result": "Draw",
                "player1score": self.player1score,
                "player2score": self.player2score}

    def playeremptymoves(self, player):
        """
        When a player does not pocket a coin for 3 successive turns he/she loses a point
        The following function checks last 3 moves of a player to see if the outcome is equal to Empty
        """

        if player == 1:
            moves = self.player1history
        else:
            moves = self.player2history

        count = 0
        j = 0

        for i in moves:
            if j > 3:
                break
            if i['outcome'] == histories.EMPTY_STRIKE:
                count = count + 1

            j = j + 1

        if count >= 3:
            self.updateplayerscore(player, -1)

    def playerfoulcount(self, player):
        """
        When a player ​fouls 3 times (a ​foul is a turn where a player loses, at least, 1 point),
        he/she loses an additional point
        The following function checks last 3 moves of a player to see if the outcome is equal to
        DEFUNCT_COIN or STRIKER_STRIKE

        """
        if player == 1:
            moves = self.player1history
        else:
            moves = self.player2history

        count = 0
        j = 0
        for i in moves:
            if j > 3:
                break
            if i['outcome'] == histories.DEFUNCT_COIN or i['outcome'] == histories.STRIKER_STRIKE:
                count = count + 1

            j = j + 1

        if count >= 3:
            self.updateplayerscore(player, -1)

    def scoredifference(self):
        """
        Gets the score difference of a players based on higher points
        """
        if self.player1score > self.player2score:
            return self.player1score - self.player2score
        else:
            return self.player2score - self.player1score