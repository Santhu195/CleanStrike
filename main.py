from random import randint
from CleanBoard import CleanBoard
from Player import Players
import outcomeConstants

with open('inputs.txt', 'w') as f:
        f.write("1. Strike \n 2.Multi Strike \n 3.Red strike \n 4.Striker strike \n 5.Defunct coin \n 6.None \n Input Outcome are \n")

class CleanStrikeGame:

    
    def checkintvalue(self,gametype):
        """
        The following checks if the value is integer and lies between 1 to 6

        """
        while True:
            try:
                if gametype == 1:
                    value = int(input())
                else:
                    value = randint(1, 6)
                    s = str(value)+'\n'
                    with open('inputs.txt', 'a+') as f:
                        f.write(s)
                    print("You Can Check the test inputs given in inputs.txt file")
            except ValueError:
                print("Please choose a proper Integer between 1 to 6")
                continue
            else:
                if value < 1 or value > 6:
                    print("Please choose a proper Integer between 1 to 6")
                    continue
                else:
                    return value
    
    def play(self,gametype):
        """
        loop keeps running until a winner is decided.
        """
        player = 1

        # Intialize the Board and Players
        cleanstrikeboard = CleanBoard()
        gameplayers = Players()

        while True:

            player = (player + 1) % 2       #to change player to 1 and 2

            if (gameplayers.checkplayerscore() and gameplayers.scoredifference() >= 3) or (
                    cleanstrikeboard.coinCheck()):

                score = gameplayers.getresult()
                print("Winner:", score['result'], "And Final Score: ", score['player1score'], '-', score['player2score'],"\n")
                #history = gameplayers.gethistorymoves()
                
                break

            print("Player ", player + 1, ": Choose an outcome from the list below")
            print("1. Strike")
            print("2. Multi Strike")
            print("3. Red strike")
            print("4. Striker strike")
            print("5. Defunct coin")
            print("6. Empty Strike")
            print("Current Coins Count on Borad")
            print("Black {} and Red {}".format(cleanstrikeboard.black,cleanstrikeboard.red))
            if gametype == 1:

                option = self.checkintvalue(gametype)

            else:

                option = self.checkintvalue(gametype)

            


            if option == 1:
                

                result = cleanstrikeboard.strike()
                gameplayers.updateplayerscore(player + 1, result)
                gameplayers.updateplayerhistory(player + 1, outcomeConstants.STRIKE)

            elif option == 2:

                result = cleanstrikeboard.multiStrike()
                gameplayers.updateplayerscore(player + 1, result)
                gameplayers.updateplayerhistory(player + 1, outcomeConstants.MULTISTRIKE)

            elif option == 3:

                result = cleanstrikeboard.redStrike()
                gameplayers.updateplayerscore(player + 1, result)
                gameplayers.updateplayerhistory(player + 1, outcomeConstants.RED_STRIKE)

            elif option == 4:

                result = cleanstrikeboard.striker()
                gameplayers.updateplayerscore(player + 1, result)
                gameplayers.updateplayerhistory(player + 1, outcomeConstants.STRIKER_STRIKE)
                gameplayers.playerfoulcount(player + 1)

            elif option == 5:

                result = cleanstrikeboard.defunt()
                gameplayers.updateplayerscore(player + 1, result)
                gameplayers.updateplayerhistory(player + 1, outcomeConstants.DEFUNCT_COIN)
                gameplayers.playerfoulcount(player + 1)

            elif option == 6:

                result = cleanstrikeboard.emptyStrike()
                gameplayers.updateplayerscore(player + 1, result)
                gameplayers.updateplayerhistory(player + 1, outcomeConstants.EMPTY_STRIKE)
                gameplayers.playeremptymoves(player + 1)



def checkoption():
    """
    The following checks if the value is integer and lies between 1 to 2
    """
    while True:
        try:
            value = int(input())
        except ValueError:
            print("Please choose a proper Integer between 1 to 2")
            continue
        else:
            if value < 1 or value > 2:
                print("Please choose a proper Integer between 1 to 2")
                continue
            else:
                return value


cleanstrike = CleanStrikeGame()
print("Choose the type of game you want to play?")
print("1. Player1 vs Player2")
print("2. StrikeBot1 vs StrikeBot2")

if checkoption() == 1:
    cleanstrike.play(1)
else:
    cleanstrike.play(2)



