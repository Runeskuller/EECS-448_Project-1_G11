class gameBoard:
	#Class Attributes
	columns = 10
	rows = 9
	
	#test change

	#Constructor: Creates a 2D array of integers with all spots marked empty(0)
	def __init__(self):
		self.board = [[int(0)]*self.columns]*self.rows

	#Returns the content of the specified tile
	def getTile(self, row, column):
		pass

	#Places a ship in the grid, represented by a number equal to the size of the ship e.g. a 1x3 ship would be three adjacent 3's on the grid
	def placeShip(self, orientation, row, column, shipSize):
		pass

	#Checks the spot on board, if there is no ship then marks it as a miss(#) and returns 0, if there is a ship then marks as a hit(X) and returns the size of the ship hit
	def shotOn(self, row, column):
		pass

	#Checks the board to see if a specific ship has been sunk. Returns true if no spaces hold the number 'shipSize'. Returns false otherwise
	def shipSunk(self, shipSize):
		pass

	#Checks if any ships are left unsunk, returns true if there are no spaces on the board representing a ship. Returns false otherwise
	def gameLost(self):
		pass

	#Prints the grid, showing ships and hits and misses
	def printPlayerView(self):
		pass

	#Prints the grid, showing only hits and misses
	def printOpponentView(self):
		pass