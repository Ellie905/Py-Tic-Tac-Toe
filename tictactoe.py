# import rich
# import random
# import pynput


# tutorial/introduction
    # once per launch


#--------------------------MAIN--------------------------#


# main function
#
# seed randoms
#
# player chooses symbol
#   # calls screen object
#
# start game (game loop below)
#
# show results
#   # calls screen object
#
# exit or restart
#   # calls screen object
#   # calls gamestate object method "wipe gamestate"
#
# end function


#--------------------------GUI--------------------------#


# screen object
#   # has string containing raw data
#
#   update method
#       # renders data using rich library
#
# screen object


# screen child object
#   # has string containing raw game data as string
#
#   update method
#       # renders game output using rich library
#
# screen child object


#--------------------------GAME DATA--------------------------#


# "table" gamestate object
#   # dictionary "table" of 9 tuples, index & character at location (x, o, or '')
#   # winner string member
#
#   export method
#       # "converts" dictionary to "raw game data" string
#
#   set caret location method
#
#   get caret location method
#
#   move caret method
#       # call "get caret location"
#       # calculate new caret location
#       # call "set caret location"
#
#   set dictionary value at caret method
#
#   check for winner method
#       # if 3-in-a-row, write winning character (x/o) to winner string member
#
#   wipe gamestate method
#       # resets caret location
#       # resets dictionary
#       # resets winner string member
#
# table gamestate object


# live input-display function aka input()
#   # uses pynput (arrow keys/enter)
#
# get player keypress
#
# if keypress is arrow keys
#   # call gamestate object method "move caret" - pass player keypress
#
# if keypress is spacebar/enter
#   # call gamestate object method "set dictionary value at caret" - pass player keypress
#
# screen child object.update method(gamestate object.export method())
#   # updates screen with new gameboard
#
# call gamestate object method "check for winner"
#
# end function


# ai input()
#
# choose random gamestate dictionary tuple with '' character inside
#   # Line up all available slots, create variable "length" based on number of slots
#   # Set random range limit to length, get random int
#   # Pick the corresponding available slot
#       # (MUCH FASTER THAN GUESS AND CHECK)
#
# call gamestate object method "set dictionary value at caret" - pass ai symbol
#
# screen child object.update method(gamestate object.export method())
#   # updates screen with new gameboard
#
# call gamestate object method "check for winner"
#
# end function


# game loop
#   # keeps track of whose turn with boolean flag "turn" (true:player|false:bot)
#
#   if it's player turn
#       # call input()
#
#   if it's AI turn
#       # call ai input()
#
#   if no winner, restart loop
#
#   update parent screen object
#
# end loop


import rich
import random
import pynput


#--------------------------GUI--------------------------#

class Screen:
    def __init__(self, rawData):
        self.data = rawData

    # Methods
    def update(self):
        # Render self.data using Rich

class GameScreen(Screen):
    # Methods
    def update(self):
        # Render self.data using Rich (Game Output)


#--------------------------GAME DATA--------------------------#

class Gamestate:
    def __init__(self):
        self.caret = 0
        self.table = [['' for x in range(3)] for y in range(3)]
        self.winner = ""

    # Methods
    def export(self):
        # Convert table to string for gameScreen object

    def moveCaret(self, input):
        # Using input, get caret location
        # calculate new location
        # call "set caret location"

    def setTableValue(self, value):
        # Using caret for table index, set mapped value to value

    def checkForWinner(self):
        self.winner = self.__checkHoriz()

        if self.winner == '':
            self.winner = self.__checkVert()

        if self.winner == '':
            self.winner = self.__checkDiag()

        return self.winner

    def wipe(self):
        self.__init__()


    #-----Private Methods-----#


    def __setCaret(self):
        # Sets caret location

    def __getCaret(self):
        # Gets caret location

    # Called by self.checkForWinner()
    def __checkHoriz(self):
        for x in range(3):
            firstLet = self.table[x][0]
            secLet = self.table[x][1]
            thirdLet = self.table[x][2]

            if firstLet == '':
                continue

            if firstLet == secLet and secLet == thirdLet:
                return firstLet  # There is a winner

        return ''

    def __checkVert(self):
        for x in range(3):
            firstLet = self.table[0][x]
            secLet = self.table[1][x]
            thirdLet = self.table[2][x]

            if firstLet == '':
                continue

            if firstLet == secLet and secLet == thirdLet:
                return firstLet  # There is a winner

        return ''

    def __checkDiag(self):
        secLet = self.table[1][1]

        firstLet = self.table[0][0]
        thirdLet = self.table[2][2]

        if firstLet != '' and firstLet == secLet and secLet == thirdLet:
            return firstLet  # There is a winner

        firstLet = self.table[0][2]
        thirdLet = self.table[2][0]

        if firstLet != '' and firstLet == secLet and secLet == thirdLet:
            return firstLet  # There is a winner

        return ''


#--------------------------MISC FUNCS--------------------------#


def playerPickSymbol():
    symbol = ''

    return symbol

def showResults(gameObj):


def askForExit():
    playerIsRestarting = True

    # Ask if player wants to exit or restart

    if playerIsRestarting:
        game.wipe()
        return True

    return False


#--------------------------MAIN--------------------------#


while True:
    # Seed Random
    random.seed()

    playerSymbol = playerPickSymbol()

    game = Gamestate()
    # Game Loop

    showResults(game)

    if askForExit() == False: # Player wants to quit
        break
