class Grid:

    m1 = "grid"

    def __init__(self):
    #creates 2D array which acts as the board
      rows, cols = (11, 11)
      self.grid = [["X" for i in range(cols)] for j in range(rows)]
      alphabet = ["A","B","C","D","E","F","G","H","I","J"]
      self.grid[0][0] = "  "
      for i in range(1,11):
          self.grid[0][i] = str(i)
          self.grid[i][0] = alphabet[i-1]

    def printBoard(self):
    #prints the board (strictly for testing purposes)
      rows, cols = (11, 11)
      for i in range(cols):
          for j in range(rows):
            print(self.grid[i][j], end = " ")
          print("\n", end = " ")

    def getStatus(self, xPos, yPos):

        return(self.grid[xPos][yPos])

    def placeShip(self, type, orientation, xPos, yPos):
        pass
        #Called when setting up the board. Takes the type of ship, along with the orientation and coordinates for the leftmost or topmost coordinate of the ship.
        
    def fireShot(self, xPos, yPos):
    #asserts whether a shot at a given coordinate is a hit or miss
        if(self.grid[xPos][yPos] == "2" or self.grid[xPos][yPos] == "3" or self.grid[xPos][yPos] == "4" or self.grid[xPos][yPos] == "5"):
            print("Hit!")
        else:
            print("Miss!")
            #checkIfSunk()

grid1 = Grid()
grid1.printBoard()
print(grid1.getStatus(1,5))

grid1.fireShot(0,4)