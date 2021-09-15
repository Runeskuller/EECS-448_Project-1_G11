class gameBoard:
	#Class Attributes
	columns = 10
	rows = 9
	
	#test change

	#Constructor: Creates a 2D array of integers with all spots marked empty(0)
	def __init__(self):
		self.board = [[int(0) for i in range(self.columns)] for j in range(self.rows)]

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
		sunk = bool(1)
		for i in range(self.rows):
			for j in range(self.columns):
				if self.board[i][j] == shipSize:
					sunk = bool(0)
		return(sunk)

	#Checks if any ships are left unsunk, returns true if there are no spaces on the board representing a ship. Returns false otherwise
	def gameLost(self):
		lost = bool(1)
		for i in range(self.rows):
			for j in range(self.columns):
				if not(self.board[i][j] == 0 or self.board[i][j] == 'X' or self.board[i][j] == '*'):
					lost = bool(0)
		return(lost)

	#Prints the grid, showing ships and hits and misses
	def printPlayerView(self):
		print("   ", end = '')
		for i in range(self.columns):
			char = chr(65+i)
			print(char, " ", end = '')

		print()

		for i in range(self.rows):
			print(i+1, " ", end = '')
			for j in range(self.columns):
				print(self.board[i][j], " ", end = '')
			print()

	#Prints the grid, showing only hits and misses
	def printOpponentView(self):
		print("   ", end = '')
		for i in range(self.columns):
			char = chr(65+i)
			print(char, " ", end = '')

		print()

		for i in range(self.rows):
			print(i+1, " ", end = '')
			for j in range(self.columns):
				if self.board[i][j] == 'X' or self.board[i][j] == '*':
					print(self.board[i][j], " ", end = '')
				else:
					print('0', " ", end = '')
			print()