class Grid:

    m1 = "grid"

    def __init__(self):
      rows, cols = (11, 11)
      self.grid = [["x" for i in range(cols)] for j in range(rows)]
      alphabet = ["A","B","C","D","E","F","G","H","I","J"]
      self.grid[0][0] = "  "
      for i in range(1,11):
          self.grid[0][i] = str(i)
          self.grid[i][0] = alphabet[i-1]
      for i in range(cols):
          for j in range(rows):
            print(self.grid[i][j], end = " ")
          print("\n", end = " ")

    def getStatus(self, xPos, yPos):
        return(self.grid[xPos][yPos])
        #Used by Executive methods to access the Grid objects.

    def placeShip(type, orientation, xPos, yPos):
        pass
        #Called when setting up the board. Takes the type of ship, along with the orientation and coordinates for the leftmost or topmost coordinate of the ship.
        
    def fireShot(xPos, yPos):
        pass
        #Checks the board after a target is selected, calls checkIfHit and updates the board appropriately to track the outcome.

grid1 = Grid()
print(grid1.getStatus(1,5))