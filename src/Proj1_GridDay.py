class Grid:

    m1 = "grid"

    def __init__(self):
    #creates 2D array which acts as the board
      rows, cols = (11, 11)
      self.grid = [["X" for i in range(cols)] for j in range(rows)]
      global alphabet
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

       
    #Called when setting up the board. Takes the type of ship, along with the orientation and coordinates for the leftmost or topmost coordinate of the ship.
    def placeShip(self, size, orientation, row, col):
        success = False
        fail = False
        while not success:
            if orientation:
                if row in alphabet and col in range(1,10):
                    if alphabet.index(row) + size < 10: 
                        for i in range(alphabet.index(row), alphabet.index(row) + size):
                            if self.grid[i+1][col] != "X":
                            #TODO: do something other than set success to true here
                                fail = True
                                
                        if fail:
                           break

                        for i in range(alphabet.index(row), alphabet.index(row) + size):
                            if self.grid[i+1][col] == "X":
                                self.grid[i+1][col] = str(size)
                                success = True
            elif not orientation:
                #TODO: Add horizontal orientation code here
                pass


        
    #asserts whether a shot at a given coordinate is a hit or miss
    def fireShot(self, xPos, yPos):
        if(self.grid[xPos][yPos] == "2" or self.grid[xPos][yPos] == "3" or self.grid[xPos][yPos] == "4" or self.grid[xPos][yPos] == "5"):
            print("Hit!")
        else:
            print("Miss!")
            #checkIfSunk()

grid1 = Grid()
grid1.printBoard()
print(grid1.getStatus(1,5))

grid1.fireShot(0,4)
grid1.placeShip(5, 1, "D", 5)
grid1.placeShip(4, 1, "A", 5 )
grid1.printBoard()