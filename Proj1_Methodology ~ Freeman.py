class Executive:

    m_player = 0

    def __init__(self):
        pass

    def setup():
        pass
        #Creates a Grid object for each player, then gives each player the option to place each ship, calling placeShip with the appropriate ship passed in when yes is selected and the placement parameters are entered.

    def togglePlayer():
        pass
        #Toggles m_player and puts up a wall to prevent the reveal of hidden information.

    def targetingScreen():
        pass
        #Checks m_player, then puts up the appropriate Grid. The player chooses a target, then fireShot is called.
        
    def checkIfHit():
        pass
        #Declares whether a shot was a hit or miss, in case of a hit it calls checkIfSunk.
        
    def checkIfSunk():
        pass
        #Declares if a ship has been sunk, if so then calls checkIfWin.
        
    def checkIfWin():
        pass
        #If the game has been won, puts up a win screen then calls endGame.
        
    def endGame():
        pass
        #Closes the game
        
class Grid:

    def __init__(self):
        pass
        
    def getStatus(xPos, yPos):
        pass
        #Used by Executive methods to access the Grid objects.

    def placeShip(type, orientation, xPos, yPos):
        pass
        #Called when setting up the board. Takes the type of ship, along with the orientation and coordinates for the leftmost or topmost coordinate of the ship.
        
    def fireShot(xPos, yPos):
        pass
        #Checks the board after a target is selected, calls checkIfHit and updates the board appropriately to track the outcome.
        